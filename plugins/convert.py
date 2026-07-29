from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    CallbackQuery
)

from helpers import (
    style_keyboard,
    get_style,
    is_media,
    format_text
)

from database import (
    set_user_style,
    get_user_style,
    add_to_sequence,
    get_sequence
)


# -----------------------------
# /convert
# -----------------------------
@Client.on_message(filters.command("convert"))
async def convert_cmd(client: Client, message: Message):

    await message.reply_text(
        "✅ Select a text style.\n\n"
        "Send any text, file, photo, video, audio or document after selecting.",
        reply_markup=style_keyboard()
    )


# -----------------------------
# Style Selection
# -----------------------------
@Client.on_callback_query(filters.regex("^style_"))
async def style_callback(client: Client, query: CallbackQuery):

    style = get_style(query.data)

    await set_user_style(
        query.from_user.id,
        style
    )

    await query.message.edit_text(
        f"✅ Style Selected : {style.title()}\n\n"
        "Now send any text or media."
    )

    await query.answer("Style Saved")


# -----------------------------
# Text Messages
# -----------------------------
@Client.on_message(
    filters.private &
    filters.text &
    ~filters.command([
        "start",
        "help",
        "convert",
        "sequence",
        "endsequence",
        "cancelsequence",
        "extractimage"
    ])
)
async def convert_text_message(client: Client, message: Message):

    style = await get_user_style(
        message.from_user.id
    )

    text = format_text(
        message.text,
        style
    )

    await message.reply_text(text)


# -----------------------------
# Media Messages
# -----------------------------
@Client.on_message(
    filters.private &
    (
        filters.photo |
        filters.video |
        filters.document |
        filters.audio |
        filters.animation
    )
)
async def media_handler(client: Client, message: Message):

    sequence = await get_sequence(
        message.from_user.id
    )

    if sequence is not None:

        await add_to_sequence(
            message.from_user.id,
            message.chat.id,
            message.id
        )

        await message.reply_text(
            f"✅ Received : {len(sequence)+1}"
        )

        return

    from helpers import format_caption


# -----------------------------
# Normal Instant Copy
# -----------------------------
    style = await get_user_style(
        message.from_user.id
    )

    caption = format_caption(
        message.caption,
        style
    )

    try:
        await client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=message.chat.id,
            message_id=message.id,
            caption=caption
        )

    except Exception as e:
        await message.reply_text(
            f"❌ Error:\n<code>{e}</code>"
        )


# -----------------------------
# Sequence Commands
# -----------------------------
@Client.on_message(filters.command("sequence"))
async def start_sequence_cmd(client, message):

    from database import start_sequence

    await start_sequence(message.from_user.id)

    await message.reply_text(
        "✅ Sequence Mode Started.\n\n"
        "Now send all your files.\n"
        "After finishing send /endsequence"
    )


@Client.on_message(filters.command("cancelsequence"))
async def cancel_sequence(client, message):

    from database import clear_sequence

    await clear_sequence(message.from_user.id)

    await message.reply_text(
        "❌ Sequence Cancelled."
    )
