from pyrogram import Client, filters
from pyrogram.types import Message

from database import (
    get_sequence,
    clear_sequence,
    get_user_style
)

from helpers import format_caption


@Client.on_message(filters.command("endsequence"))
async def end_sequence(client: Client, message: Message):

    files = await get_sequence(
        message.from_user.id
    )

    if not files:
        return await message.reply_text(
            "❌ No files found in sequence."
        )

    style = await get_user_style(
        message.from_user.id
    )

    status = await message.reply_text(
        f"📤 Sending 0/{len(files)}..."
    )

    total = len(files)

    for index, data in enumerate(files, start=1):

        try:

            msg = await client.get_messages(
                data["chat_id"],
                data["message_id"]
            )

            caption = format_caption(
                msg.caption,
                style
            )

            await client.copy_message(
                chat_id=message.chat.id,
                from_chat_id=data["chat_id"],
                message_id=data["message_id"],
                caption=caption
            )

            await status.edit_text(
                f"📤 Sending {index}/{total}..."
            )

        except Exception as e:

            print(e)

    await clear_sequence(
        message.from_user.id
    )

    await status.edit_text(
        "✅ Sequence Completed Successfully."
    )
