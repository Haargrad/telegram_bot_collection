import os
import tempfile
import praw
import youtube_dl
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from moviepy.editor import VideoFileClip

TELEGRAM_TOKEN = ''
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent='telegram:my_bot:v0.0.1 (by u/your_username)')

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Send me a Reddit URL!')

def download_and_convert_webm(update: Update, context: CallbackContext):
    url = update.message.text
    if url.endswith('.webm'):
        response = requests.get(url)

        with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as webm_file:
            webm_file.write(response.content)
            webm_file.flush()
            webm_path = webm_file.name

        video = VideoFileClip(webm_path)
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as mp4_file:
            video.write_videofile(mp4_file.name, codec="libx264", audio_codec='aac')
            mp4_file.flush()
            mp4_path = mp4_file.name

        with open(mp4_path, 'rb') as video_file:
            update.message.reply_video(video=video_file, quote=True)

        os.remove(webm_path)
        os.remove(mp4_path)

def download_reddit_content(update: Update, context: CallbackContext):
    url = update.message.text

    if "reddit.com" not in url:
        return

    submission = reddit.submission(url=url)

    if submission.is_video:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'temp_video.%(ext)s',
            'quiet': True
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open('temp_video.mp4', 'rb') as video_file:
            update.message.reply_video(video=video_file, quote=True)

        os.remove('temp_video.mp4')

    elif submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        update.message.reply_photo(submission.url, quote=True)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex(r".*\.webm$"), download_and_convert_webm))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(r".*\.webm$"), download_reddit_content))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
