from pyrogram.types import InlineKeyboardButton

import config
from Dfschinnamusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["💗𝐀𝐃𝐃 𝐦𝐞 𝐛𝐚𝐛𝐲💓"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["💗sᴜᴘᴘᴏʀᴛ💗"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["💗𝐀𝐃𝐃 𝐦𝐞 𝐛𝐚𝐛𝐲💓"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["💗ᴄᴏᴍᴍᴀɴᴅs💗"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["💗ᴅᴇᴠ💗"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["💗ᴄʜᴀɴɴᴇʟ💗"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons
