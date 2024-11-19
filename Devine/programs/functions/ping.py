from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from Dev import app
from Devine.root.call import Devine as Devine
from Devine.utils import bot_sys_stats
from Devine.utils.decorators.language import language
from Devine.utils.inline import supp_markup
from configuration import filter_users

@app.on_message(filters.command(["ping"]) & ~filter_users)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_text(
        text=_["ping_1"].format(app.mention),
    )
    pytgping = await Devine.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=SUPPORT_CHANNEL),
                InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            ],
            [
                InlineKeyboardButton(text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=true"),
            ],
        ])
    )
