import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import ChatPermissions
from pyrogram import filters
from pyrogram.types import Message


from Dev import app
from Devine.root.call import Devine
from Devine.utils import bot_sys_stats
from Devine.utils.decorators.language import language
from Devine.utils.inline import supp_markup
from configuration import filter_users, PING_IMG_URL, OWNER_ID


@app.on_message(filters.command("status") & ~filter_users)
@language
async def status_com(client, message: Message, _):
    if message.from_user.id != OWNER_ID:
        await message.reply_text(
            "<b>ᴋɪᴅ ɢʀᴏᴡ ᴜᴘ ғɪʀsᴛ.\nʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴄᴀᴘᴀʙʟᴇ ᴇɴᴏᴜɢʜ ᴛᴏ ᴅᴏ ᴛʜɪs.</b>"
        )
        return


    try:
        UP, CPU, RAM, DISK = await bot_sys_stats()
        status_message = (
            f"<b>sʏsᴛᴇᴍ sᴛᴀᴛᴜs :</b>\n\n"
            f"‣ ᴜᴩᴛɪᴍᴇ : {UP}\n"
            f"‣ ᴄᴘᴜ : {CPU}\n"
            f"‣ ʀᴀᴍ : {RAM}\n"
            f"‣ ᴅɪsᴋ : {DISK}\n\n"
           
        )


        if PING_IMG_URL:
            await message.reply_photo(photo=PING_IMG_URL, caption=status_message, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Devine_Community")]]))
        else:
            await message.reply_text(status_message, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Devine_Community")]]))
            
        # Protect the message by setting permissions
        if message.chat.type in ["group", "supergroup"]:
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(can_delete_messages=False)
            )
        
    except Exception as e:
        await message.reply_text(f"<b>Something went wrong:</b> {e}")




# Remove restrictions after a while if necessary
@app.on_message(filters.command("unrestrict") & ~filter_users)
@language
async def unrestrict(client, message: Message, _):
    if message.from_user.id == OWNER_ID:
        await client.restrict_chat_member(
            message.chat.id,
            message.from_user.id,
            ChatPermissions(can_delete_messages=False)
        )
        await message.reply_text("User restrictions lifted.")
