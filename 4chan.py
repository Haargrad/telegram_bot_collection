import os
import tempfile
import random
import datetime
import requests
import json
from datetime import timedelta
from moviepy.editor import VideoFileClip
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TELEGRAM_TOKEN = ''
board = 'wsg'

def save_subscribers(subscribers):
    with open("subscribers.json", "w") as file:
        json.dump(subscribers, file)

def load_subscribers():
    try:
        with open("subscribers.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def get_random_4chan_media(board):
    url = f"https://a.4cdn.org/{board}/catalog.json"
    response = requests.get(url)
    data = response.json()
    
    random_page = random.choice(data)
    random_thread = random.choice(random_page["threads"])
    thread_id = random_thread["no"]
    
    url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"
    response = requests.get(url)
    thread_data = response.json()
    
    posts_with_media = [post for post in thread_data["posts"] if "tim" in post and "ext" in post]
    
    if not posts_with_media:
        return None, None
    
    random_post = random.choice(posts_with_media)
    media_id = random_post["tim"]
    media_ext = random_post["ext"]
    media_url = f"https://i.4cdn.org/{board}/{media_id}{media_ext}"
    
    if media_ext in [".webm", ".mp4"]:
        media_type = "video"
    elif media_ext in [".jpg", ".jpeg", ".png", ".gif"]:
        media_type = "image"
    else:
        media_type = None
    
    return media_url, media_type

def convert_webm_to_mp4(input_path, output_path):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec="libx264")

def is_time_in_range(start, end):
    current_time = datetime.datetime.now().time()
    current_time_str = current_time.strftime("%H:%M:%S")
    return start <= current_time_str <= end

def should_send_media(now, last_sent_time, interval):
    delta = now - last_sent_time
    if interval[-1] == "m":
        interval_minutes = int(interval[:-1])
        return delta.total_seconds() >= interval_minutes * 60
    elif interval[-1] == "h":
        interval_hours = int(interval[:-1])
        return delta.total_seconds() >= interval_hours * 3600
    else:
        return False

def schedule_random_media(context: CallbackContext):
    start_time = "08:00:00"
    end_time = "21:00:00"

    if is_time_in_range(start_time, end_time):
        now = datetime.datetime.now()
        for chat_id, interval in subscribed_chats.items():
            # Проверьте, сколько времени прошло с момента последней отправки
            last_sent_time = last_sent_times.get(chat_id, None)
            if not last_sent_time or should_send_media(now, last_sent_time, interval):
                send_random_4chan_media(context, chat_id)
                last_sent_times[chat_id] = now

subscribed_chats = {}
last_sent_times = {}

subscribed_chats = load_subscribers()

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    interval = context.args[0] if context.args else "1m"  # Используйте аргументы или значение по умолчанию (1 минута)
    subscribed_chats[chat_id] = interval
    save_subscribers(subscribed_chats)  # Сохраните подписчиков в файл
    update.message.reply_text(f'Вы подписались на рассылку видео с интервалом {interval}.')

def stop(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if chat_id in subscribed_chats:
        del subscribed_chats[chat_id]
        save_subscribers(subscribed_chats)
        update.message.reply_text("Вы успешно отписались от рассылки.")
    else:
        update.message.reply_text("Вы не подписаны на рассылку.")

def send_random_4chan_media_command(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    send_random_4chan_media(context, chat_id)

def send_random_4chan_media(context: CallbackContext, chat_id):
    media_url, media_type = get_random_4chan_media(board)

    if media_url and media_type:
        if media_type == "image":
            context.bot.send_photo(chat_id=chat_id, photo=media_url)
        elif media_type == "video":
            response = requests.get(media_url)
            webm_file = tempfile.NamedTemporaryFile(delete=False, suffix=".webm")
            webm_file.write(response.content)
            webm_file.close()

            mp4_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
            convert_webm_to_mp4(webm_file.name, mp4_file.name)

            with open(mp4_file.name, 'rb') as video:
                context.bot.send_video(chat_id=chat_id, video=video)

            os.unlink(webm_file.name)
            os.unlink(mp4_file.name)
    else:
        print(f"Ошибка при отправке медиа в чат {chat_id}: {e}")


def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("random4chan", send_random_4chan_media_command))
    dispatcher.add_handler(CommandHandler("start", start))
    job_queue = updater.job_queue
    interval = timedelta(minutes=1)
    job_queue.run_repeating(schedule_random_media, interval=interval)
    dispatcher.add_handler(CommandHandler("stop", stop))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
