import requests
import random
import openai
import aiohttp
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


token = 'TELEGRAM_TOKEN'
openai.api_key = 'OPENAI_TOKEN'

bot = Bot(token)
dp = Dispatcher(bot)

async def generate_response(message: types.Message):
    bot_username = (await bot.me).username.lower()

    def create_response(prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["You:"]
        )
        return response['choices'][0]['text']

    should_generate_response = (
        bot_username in message.text.lower()
        or random.randint(1, 200) == 200
        or (message.reply_to_message and message.reply_to_message.from_user.username.lower() == bot_username)
    )

    if should_generate_response:
        await message.reply(create_response(message.text))
    else:
        return


@dp.message_handler()
async def process_message(message: types.Message):
    await generate_response(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
