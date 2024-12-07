from pyrogram.types import InlineKeyboardButton
import configuration
from Dev import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=configuration.SUPPORT_CHAT),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=configuration.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=configuration.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"),
        ]
    ]
    return buttons
