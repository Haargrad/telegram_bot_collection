import os
import random
import tempfile
import requests
import youtube_dl
import datetime
import json
from datetime import timedelta
from telegram import Update, InputMediaVideo
from telegram.ext import Updater, CommandHandler, CallbackContext

SUBSCRIBERS_FILE = "subscribers.json"
TELEGRAM_TOKEN = ''

subscribed_chats = {}
last_sent_times = {}

def should_send_video(now, last_sent_time, interval):
    delta = now - last_sent_time
    return delta >= interval

def is_time_in_range(start, end):
    now = datetime.datetime.now().time()
    start_time = datetime.datetime.strptime(start, '%H:%M:%S').time()
    end_time = datetime.datetime.strptime(end, '%H:%M:%S').time()
    return start_time <= now <= end_time

def schedule_random_video(context: CallbackContext):
    start_time = "08:00:00"
    end_time = "21:00:00"

    if is_time_in_range(start_time, end_time):
        now = datetime.datetime.now()
        for chat_id, interval in subscribed_chats.items():
            last_sent_time = last_sent_times.get(chat_id, None)
            if not last_sent_time or should_send_video(now, last_sent_time, interval):
                send_video(chat_id, context)
                last_sent_times[chat_id] = now

def parse_interval(interval_str):
    if interval_str[-1].lower() == 'm':
        return timedelta(minutes=int(interval_str[:-1]))
    elif interval_str[-1].lower() == 'h':
        return timedelta(hours=int(interval_str[:-1]))
    elif interval_str[-1].lower() == 'd':
        return timedelta(days=int(interval_str[:-1]))
    else:
        raise ValueError(f"Invalid interval format: {interval_str}")

def get_random_2hk_video_url():
    response = requests.get('https://2ch.hk/b/threads.json')
    data = response.json()

    threads = [t for t in data['threads'] if 'webm' in t['subject'].lower() and not any(x in t['subject'].lower() for x in ['anime', 'аниме', 'музыка', 'music'])]

    if threads:
        random_thread = random.choice(threads)
        thread_id = random_thread['num']

        response = requests.get(f'https://2ch.hk/b/res/{thread_id}.json')
        data = response.json()

        video_posts = [p for p in data['threads'][0]['posts'] if 'files' in p and p['files']]

        if video_posts:
            random_video_post = random.choice(video_posts)
            video_path = random_video_post['files'][0]['path'] if random_video_post['files'] else None
            if video_path:
                return f'https://2ch.hk{video_path}'

    return None

def send_video(chat_id, context: CallbackContext):
    video_url = get_random_2hk_video_url()
    if video_url:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'temp_video.%(ext)s',
            'quiet': True
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            file_name = ydl.prepare_filename(info)

        with open(file_name, 'rb') as video_file:
            context.bot.send_video(chat_id=chat_id, video=video_file)

        os.remove(file_name)
    else:
        context.bot.send_message(chat_id=chat_id, text='Не удалось получить видео. Попробуйте еще раз.')

def parse_interval(interval_str):
    if ':' in interval_str:
        time_parts = interval_str.split(':')
        hours, minutes, seconds = int(time_parts[0]), int(time_parts[1]), int(time_parts[2])
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    elif interval_str[-1].lower() == 'm':
        return timedelta(minutes=int(interval_str[:-1]))
    elif interval_str[-1].lower() == 'h':
        return timedelta(hours=int(interval_str[:-1]))
    elif interval_str[-1].lower() == 'd':
        return timedelta(days=int(interval_str[:-1]))
    else:
        raise ValueError(f"Invalid interval format: {interval_str}")


def load_subscribers():
    global subscribed_chats
    if os.path.exists(SUBSCRIBERS_FILE):
        with open(SUBSCRIBERS_FILE, "r") as f:
            subscribed_chats = json.load(f)
            for chat_id in subscribed_chats:
                subscribed_chats[chat_id] = parse_interval(subscribed_chats[chat_id])

def save_subscribers():
    with open(SUBSCRIBERS_FILE, "w") as f:
        data = {chat_id: str(interval) for chat_id, interval in subscribed_chats.items()}
        json.dump(data, f)

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    interval_str = context.args[0] if context.args else "1m"
    interval = parse_interval(interval_str)
    subscribed_chats[chat_id] = interval
    save_subscribers()  # Сохраняем подписчиков при подписке
    update.message.reply_text(f'Вы подписались на рассылку видео с интервалом {interval_str}.')

def stop(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if chat_id in subscribed_chats:
        del subscribed_chats[chat_id]
        save_subscribers()
        update.message.reply_text('Вы успешно отписались от рассылки видео.')
    else:
        update.message.reply_text('Вы не подписаны на рассылку видео.')

def main():
    load_subscribers()
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    job_queue = updater.job_queue
    interval = timedelta(minutes=1)
    job_queue.run_repeating(schedule_random_video, interval=interval)
    dispatcher.add_handler(CommandHandler("video", send_video))
    dispatcher.add_handler(CommandHandler("stop", stop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
