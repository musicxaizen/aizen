from pyrogram import filters
from pyrogram.types import Message

from Dev import app
from Devine.misc import SUDOERS
from Devine.utils.database import blacklist_chat, blacklisted_chats, whitelist_chat
from configuration import filter_users, OWNER_ID


@app.on_message(filters.command(["leave"]) & filters.user(OWNER_ID))
async def blacklist_chat_func(client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴄʜᴀᴛ ɪᴅ ᴛᴏ ʙʟᴀᴄᴋʟɪsᴛ.")
    
    chat_id = int(message.text.strip().split()[1])
    
    if chat_id in await blacklisted_chats():
        return await message.reply_text("ᴛʜɪs ᴄʜᴀᴛ ɪs ᴀʟʀᴇᴀᴅʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ.")
    
    blacklisted = await blacklist_chat(chat_id)
    
    if blacklisted:
        await message.reply_text("ᴄʜᴀᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ.")
    else:
        await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ʙʟᴀᴄᴋʟɪsᴛ ᴛʜᴇ ᴄʜᴀᴛ.")
    
    try:
        await app.leave_chat(chat_id)
    except:
        pass


@app.on_message(filters.command(["whitelistchat", "unblacklistchat", "unblchat"]) & SUDOERS)
async def white_funciton(client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴄʜᴀᴛ ɪᴅ ᴛᴏ ᴡʜɪᴛᴇʟɪsᴛ.")
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats():
        return await message.reply_text("ᴛʜɪs ᴄʜᴀᴛ ɪs ɴᴏᴛ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ.")
    whitelisted = await whitelist_chat(chat_id)
    if whitelisted:
        return await message.reply_text("ᴄʜᴀᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴡʜɪᴛᴇʟɪsᴛᴇᴅ.")
    await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴡʜɪᴛᴇʟɪsᴛ ᴛʜᴇ ᴄʜᴀᴛ.")


@app.on_message(filters.command(["blchats", "blacklistedchats"]) & SUDOERS)
async def all_chats(client, message: Message):
    text = "<b>ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛs:</b>\n\n"
    j = 0
    for count, chat_id in enumerate(await blacklisted_chats(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except:
            title = "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        j = 1
        text += f"{count}. {title}[<code>{chat_id}</code>]\n"
    if j == 0:
        await message.reply_text("ɴᴏ ᴄʜᴀᴛs ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ.")
    else:
        await message.reply_text(text)
