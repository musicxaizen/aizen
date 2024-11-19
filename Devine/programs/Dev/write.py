from pyrogram import filters
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from datetime import datetime
from Dev import app as app
import requests

@app.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "<b>ʜᴏʟᴅ ᴏɴ,\nᴡʀɪᴛɪɴɢ ʏᴏᴜʀ ᴛᴇxᴛ...</b>")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
<b>sᴜᴄᴇssғᴜʟʟʏ ᴛᴇxᴛ ᴡʀɪᴛᴛᴇɴ, ✨</b>

<b>• ᴡʀɪᴛᴛᴇɴ ʙʏ : </b>{app.mention}
<b>• ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : </b>{message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)
