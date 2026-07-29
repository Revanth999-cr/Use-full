from pyrogram import Client, filters
from pyrogram.types import Message
import os
import tempfile


@Client.on_message(filters.command("extractimage"))
async def extract_image(client: Client, message: Message):

    if not message.reply_to_message:
        return await message.reply_text(
            "❌ Reply to a photo, video or document."
        )

    media = message.reply_to_message

    if media.photo:
        await client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=media.chat.id,
            message_id=media.id
        )
        return

    target = media.video or media.document or media.animation

    if not target:
        return await message.reply_text(
            "❌ No thumbnail found."
        )

    if not target.thumbs:
        return await message.reply_text(
            "❌ This file doesn't contain a thumbnail."
        )

    temp = tempfile.mkdtemp()

    thumb = await client.download_media(
        target.thumbs[0].file_id,
        file_name=os.path.join(temp, "thumb.jpg")
    )

    await message.reply_photo(
        thumb,
        caption="🖼 Extracted Thumbnail"
    )

    try:
        os.remove(thumb)
        os.rmdir(temp)
    except:
        pass
