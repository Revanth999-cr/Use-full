from pyrogram import Client, filters
from pyrogram.types import Message

from helpers import style_keyboard
from config import BOT_NAME


@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    text = f"""
👋 Welcome to **{BOT_NAME}**

I can instantly convert:
• Text
• File Captions
• Photo Captions
• Video Captions
• Audio Captions
• Documents

📌 Commands:
/convert - Select a font style
/sequence - Start sequence mode
/endsequence - Send all queued files
/cancelsequence - Cancel current sequence
/extractimage - Extract thumbnail from a replied media file
/help - Show help
"""

    await message.reply_text(
        text,
        reply_markup=style_keyboard(),
        disable_web_page_preview=True
    )


@Client.on_message(filters.command("help"))
async def help_handler(client: Client, message: Message):
    await message.reply_text(
        """
📖 **Help**

/convert
• Choose Bold / Italic / Mono.

After selecting a style, send:
• Text
• Photo
• Video
• Audio
• Document

The bot will automatically convert the text/caption and send it back.

📦 Sequence Mode

/sequence
Start collecting files.

/endsequence
Resend all collected files in the same order.

/cancelsequence
Clear the current sequence.

🖼 Extract Image

Reply to a media message with:
/extractimage

The bot will send the thumbnail/cover image if available.
"""
    )
