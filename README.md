# Bold Converter Bot

A Telegram bot that instantly converts text and media captions into stylish Unicode fonts.

## Features

- Convert text instantly
- Convert captions instantly
- Bold, Italic and Mono styles
- Sequence Mode
- End Sequence
- Cancel Sequence
- Extract Thumbnail
- MongoDB Support
- Docker Ready
- Render Ready

## Commands

/start

/help

/convert

/sequence

/endsequence

/cancelsequence

/extractimage

## Setup

Clone the repository

```bash
git clone <your-repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Edit `config.py`

```python
API_ID = ...
API_HASH = "..."
BOT_TOKEN = "..."
MONGO_URI = "..."
OWNER_ID = ...
```

Run the bot

```bash
python bot.py
```

## Docker

Build

```bash
docker build -t boldconverter .
```

Run

```bash
docker run boldconverter
```

## Credits

Developed using Pyrogram and MongoDB.
