# Telegram BOT collection

bot - chat bots

Download bot.py

```bash
pip install aiohttp random python-telegram-bot requests openai
```

Set 'TELEGRAM_TOKEN' and 'OPENAI_TOKEN'

start bot

virus.py - bot to analyze links and files for malware

video.py- bot for downloading and converting videos from reddit


# 2ch Video Bot

This Telegram bot sends random videos from the 2ch.hk/b board to users who have subscribed to its mailing list.

## Key Features

1. Send random videos from the 2ch.hk/b board.
2. Ability to subscribe to a video mailing list with a specified interval.
3. Time restrictions for sending videos (from 8:00 AM to 9:00 PM).

## Installation and Setup

1. Ensure you have Python 3.6 or higher installed.
2. Install the required dependencies 
3. Create a new Telegram bot via [@BotFather](https://t.me/BotFather) and obtain the access token.
4. Replace the \`TELEGRAM_TOKEN\` in the \`2ch-random.py\` file with the access token you received.

## Running the Bot

Run the bot by executing the following command:

\`\`\`
python3 2ch-random.py
\`\`\`

## Usage

1. Find your bot on Telegram by the name you provided during its creation.
2. Press the \`/start\` button or enter the command \`/start [interval]\`, where \`[interval]\` is the interval between sending videos (e.g., \`1m\`, \`2h\`, or \`1d\`). If the interval is not specified, the default value of \`1m\` will be used.
3. The bot will start sending videos with the specified interval. If you want to receive a video immediately, enter the command \`/video\`.

## Interval Format

The interval should be specified as a string with a number followed by one of the following letters:

- \`m\` for minutes (e.g., \`15m\` means 15 minutes)
- \`h\` for hours (e.g., \`2h\` means 2 hours)
- \`d\` for days (e.g., \`1d\` means 1 day)

## License

This project is available under the MIT License.
