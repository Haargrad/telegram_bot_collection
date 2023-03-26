# Telegram BOT collection

# 1. DaVinci Telegram Bot

This Telegram bot uses OpenAI's GPT-3 model, specifically the "text-davinci-003" model, to generate and send intelligent responses to user messages in a chat.

## Key Features

1. Generate intelligent responses using OpenAI's GPT-3 model.
2. Respond to messages that mention the bot's username.
3. Respond randomly with a 1 in 200 chance for each received message.
4. Respond to messages that are replies to the bot's messages.

## Installation and Setup

1. Ensure you have Python 3.6 or higher installed.
2. Install the required dependencies
3. Create a new Telegram bot via [@BotFather](https://t.me/BotFather) and obtain the access token.
4. Replace the `TELEGRAM_TOKEN` in the `bot-davinci.py` file with the access token you received.
5. Sign up for an [OpenAI API key](https://beta.openai.com/signup/) and replace the `OPENAI_TOKEN` in the `bot-davinci.py` file with your API key.

## Running the Bot

Run the bot by executing the following command:

```bash
python3 bot-davinci.py
```

# 2. GPT-3.5 Turbo Telegram Bot

This Telegram bot uses OpenAI's GPT-3.5 Turbo model to generate and send intelligent responses to user messages in a chat.

## Key Features

1. Generate intelligent responses using OpenAI's GPT-3.5 Turbo model.
2. Respond to messages that mention the bot's username.
3. Respond randomly with a 1 in 1000 chance for each received message.
4. Respond to messages that are replies to the bot's messages.

## Installation and Setup

1. Ensure you have Python 3.6 or higher installed.
2. Install the required dependencies
3. Create a new Telegram bot via [@BotFather](https://t.me/BotFather) and obtain the access token.
4. Replace the `TELEGRAM_TOKEN` in the bot script with the access token you received.
5. Sign up for an [OpenAI API key](https://beta.openai.com/signup/) and replace the `OPENAI_TOKEN` in the bot script with your API key.

## Running the Bot

Run the bot by executing the following command:

```bash
python3 bot-gpt3.5-turbo.py
```

# 3. video.py Reddit Content Telegram Bot

This Telegram bot allows users to download and share Reddit content, including images, GIFs, and videos.

## Key Features

1. Download and share Reddit content (images, GIFs, and videos).
2. Convert `.webm` files to `.mp4` for compatibility with Telegram.

## Installation and Setup

1. Ensure you have Python 3.6 or higher installed.
2. Install the required dependencies 
3. Create a new Telegram bot via [@BotFather](https://t.me/BotFather) and obtain the access token.
4. Replace the `TELEGRAM_TOKEN` in the bot script with the access token you received.
5. Sign up for a [Reddit API client](https://www.reddit.com/prefs/apps) and obtain the `client_id` and `client_secret`.
6. Replace the `CLIENT_ID` and `CLIENT_SECRET` in the bot script with your Reddit API credentials.

## Running the Bot

Run the bot by executing the following command:

```bash
python3 video.py
```

# 4. virus.py URL Safety Checker Telegram Bot

This Telegram bot checks the safety of a URL using the VirusTotal API.

## Key Features

1. Analyze URLs for potential threats using the VirusTotal API.
2. Notify users if a URL is considered malicious or suspicious.

## Installation and Setup

1. Ensure you have Python 3.6 or higher installed.
2. Install the required dependencies 
3. Create a new Telegram bot via [@BotFather](https://t.me/BotFather) and obtain the access token.
4. Replace the `TELEGRAM_TOKEN` in the bot script with the access token you received.
5. Sign up for a [VirusTotal API](https://developers.virustotal.com/reference) key.
6. Replace the `API_KEY` in the bot script with your VirusTotal API key.

## Running the Bot

Run the bot by executing the following command:

```bash
python3 virus.py
```

# 4. 2ch Video Bot

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

```bash
python3 2ch-random.py
```

## Usage

1. Find your bot on Telegram by the name you provided during its creation.
2. Press the \`/start\` button or enter the command \`/start [interval]\`, where \`[interval]\` is the interval between sending videos (e.g., \`1m\`, \`2h\`, or \`1d\`). If the interval is not specified, the default value of \`1m\` will be used.
3. The bot will start sending videos with the specified interval. If you want to receive a video immediately, enter the command \`/video\`.

## Interval Format

The interval should be specified as a string with a number followed by one of the following letters:

- \`m\` for minutes (e.g., \`15m\` means 15 minutes)
- \`h\` for hours (e.g., \`2h\` means 2 hours)
- \`d\` for days (e.g., \`1d\` means 1 day)

# Telegram Bot: 4chan Media Scheduler

This Telegram bot is designed to fetch random media from a specified 4chan board and send it to subscribed users at a specified interval.

## Features

- Fetch random media (images and videos) from a specified 4chan board
- Convert .webm videos to .mp4 format
- Subscribe users to receive media at specified intervals
- Send media only during a specific time range

## Dependencies

- moviepy
- requests
- python-telegram-bot

## Usage

1. Install the required dependencies:

```bash
pip install moviepy requests python-telegram-bot
```

2. Replace TELEGRAM_TOKEN with your bot's API token.

3. Run the script:

```bash
python3 4chan.py
```

4. Interact with the bot using the following commands:

/start <interval> - Subscribe to the bot's media feed. The interval can be specified with "m" for minutes or "h" for hours (e.g., "5m" or "2h"). Default interval is 1 minute.

The board can be changed by entering the desired value in the variable board = 'wsg'

/random4chan - Send a random media from the specified board immediately.

How it works
The bot fetches the catalog of the specified board and chooses a random thread.
It then selects a random post with media from the thread.
If the media is a video in .webm format, it converts it to .mp4.
The bot sends the media to the subscribed chat.
The bot checks the specified interval and sends media only during the specified time range.
Note
The code has been provided in Russian. Make sure to translate the text to the desired language before using the bot.

## License

This project is available under the MIT License.
