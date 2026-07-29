# helpers.py

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fonts import convert_text


def style_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝗕𝗼𝗹𝗱", callback_data="style_bold"),
                InlineKeyboardButton("𝘐𝘵𝘢𝘭𝘪𝘤", callback_data="style_italic"),
            ],
            [
                InlineKeyboardButton("𝙼𝚘𝚗𝚘", callback_data="style_mono"),
            ]
        ]
    )


def get_style(callback_data: str) -> str:
    return callback_data.replace("style_", "")


def format_caption(caption: str | None, style: str) -> str | None:
    if not caption:
        return None
    return convert_text(caption, style)


def format_text(text: str | None, style: str) -> str:
    if not text:
        return ""
    return convert_text(text, style)


def is_media(message):
    return any([
        message.photo,
        message.video,
        message.document,
        message.audio,
        message.voice,
        message.animation,
        message.video_note
    ])
