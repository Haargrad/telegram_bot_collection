# Telegram BOT collection

# DaVinci Telegram Bot

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
python bot-davinci.py
```

## Usage

1. Find your bot on Telegram by the name you provided during its creation.
2. Start a conversation with the bot, and it will respond intelligently to messages that mention its username, are replies to its messages, or randomly with a 1 in 200 chance for each received message.

## License

This project is available under the MIT License.
















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

## License

This project is available under the MIT License.
