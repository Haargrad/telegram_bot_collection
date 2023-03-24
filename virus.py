import os
import io
import praw
import tempfile
import requests
import youtube_dl
from moviepy.editor import concatenate_audioclips, AudioFileClip, VideoFileClip
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TELEGRAM_TOKEN = ''
API_KEY = ""

def check_url_virustotal(url):
    headers = {
        "x-apikey": API_KEY
    }

    data = {
        "url": url
    }

    response = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data=data)

    if response.status_code == 200:
        json_response = response.json()
        url_id = json_response['data']['id']
        
        analysis_response = requests.get(f"https://www.virustotal.com/api/v3/analyses/{url_id}", headers=headers)
        if analysis_response.status_code == 200:
            analysis_json = analysis_response.json()
            malicious_engines = 0
            total_engines = 0
            for engine, result in analysis_json['data']['attributes']['results'].items():
                total_engines += 1
                if result['category'] in ['malicious', 'suspicious']:
                    malicious_engines += 1

            safety_threshold = 0.1
            if total_engines > 0 and (malicious_engines / total_engines) <= safety_threshold:
                return True
            else:
                return False
        else:
            print(f"Error while getting analysis results: {analysis_response.status_code}")
            return None
    else:
        print(f"Error while getting analysis results: {response.status_code}")
        return None

def handle_text(update: Update, context: CallbackContext):
    url = update.message.text
    if not check_url_virustotal(url):
        update.message.reply_text("⚠️ The URL may be malicious. be careful.")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
