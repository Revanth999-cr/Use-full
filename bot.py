import logging
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] %(message)s"
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)

app = Client(
    "BoldConverterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    app.start()
    me = app.get_me()
    print("=" * 50)
    print(f"Bot Started Successfully!")
    print(f"Name : {me.first_name}")
    print(f"Username : @{me.username}")
    print("=" * 50)
    idle()
    app.stop()
