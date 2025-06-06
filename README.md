# Basic Telegram Bot in Python

This is a simple Telegram bot that responds to the `/start` command with a custom message. I created this as a starting point for anyone wanting to build their own Telegram bot.

## Prerequisites

You'll need a few things before getting started:

- Python 3.7 or higher installed on your system
- The `python-telegram-bot` library

Install the library using pip:

```bash
pip install python-telegram-bot --upgrade
```

## Setting up the bot

### Getting your bot token

First, you need to create a bot and get an API token from Telegram:

1. Open Telegram and search for the official `@BotFather` bot
2. Send the command `/newbot`
3. Choose a name and username for your bot
4. BotFather will give you an API token (a long string of characters)
5. Keep this token private and secure

### Adding the token to your code

In your Python script, replace this line:

```python
app = ApplicationBuilder().token("YOUR_TOKEN_HERE").build()
```

with your actual token:

```python
app = ApplicationBuilder().token("123456789:ABCdefGhIjkLmnoPQRstuVwxYZ").build()
```

## Running the bot

To start your bot, run the Python script in your terminal:

```bash
python bot.py
```

If everything is set up correctly, you should see:

```
Bot started
```

## How to use it

Once your bot is running:

1. Find your bot on Telegram using its username
2. Send `/start` to the bot
3. The bot will respond with your predefined message

## Customizing your bot

You can easily modify the `start` function in the script to change what the bot says or add new features. This is just the foundation - you can build much more complex functionality from here.

## Project structure

Here's how I organized the files:

```
telegram-bot/
├── bot.py           # Main bot script
├── README.md        # This file
└── requirements.txt # Dependencies (optional)
```

## Dependencies

If you want to create a `requirements.txt` file for easier setup:

```
python-telegram-bot>=20.0
```

## License

Feel free to use this code however you want. I'm releasing it under the MIT License.

## Questions or issues

If you run into any problems or have questions, feel free to reach out. I'm happy to help!

---

**Security note:** Never share your API token publicly. In production environments, consider using environment variables to store sensitive information like tokens.
