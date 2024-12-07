import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from configuration import OWNER_ID
from Dev import app
import configuration 

@app.on_message(filters.command("alive"))
async def awake(_, message: Message):
    loading_1 = await message.reply_text("⚡")
    await asyncio.sleep(0.1)

    loading_texts = [
        "<b>ʟᴏᴀᴅɪɴɢ</b>",
        "<b>ʟᴏᴀᴅɪɴɢ.</b>",
        "<b>ʟᴏᴀᴅɪɴɢ..</b>",
        "<b>ʟᴏᴀᴅɪɴɢ...</b>"
    ]

    for text in loading_texts:
        await loading_1.edit_text(text)
        await asyncio.sleep(1)  
    
    await loading_1.delete()

    owner = await app.get_users(OWNER_ID)
    
    if message.from_user.id == OWNER_ID:
        TEXT = "ɪ'ᴍ ᴀʟɪᴠᴇ ᴍʏ ʟᴏʀᴅ <a href='https://envs.sh/5Ci.jpg' target='_blank'>⚡</a> !\n\n"
    else:
        TEXT = f"ʏᴏᴏ {message.from_user.mention}, <a href='https://envs.sh/5Ci.jpg' target='_blank'>⚡</a>\n\nɪ'ᴍ {app.mention}\n──────────────────\n"
    
    TEXT += f"ᴄʀᴇᴀᴛᴏʀ ⌯ {owner.mention}\n"
    TEXT += f"ᴠᴇʀsɪᴏɴ ⌯ 𝟸.𝟷𝟼\n"
    TEXT += f"ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ⌯ 𝟹.𝟷𝟸.𝟶\n"
    TEXT += f"ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ ⌯ 𝟸.𝟶.𝟷𝟶𝟼"
    
    BUTTON = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=configuration.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=configuration.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ", url="https://t.me/Soul_musixbot?startgroup=true"),
    ],
    ]    
    
    await message.reply_text(
        text=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )
