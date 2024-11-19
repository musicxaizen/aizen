from pyrogram import filters
from pyrogram.types import Message
from Devine import app
from config import BANNED_USERS, OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

OWNER_ID = 6440363814

@app.on_message(filters.command(["repo", "source"]) & ~BANNED_USERS)
async def repo(client, message: Message):
    user_mention = message.from_user.mention if message.from_user else "Unknown User"
    user_id = message.from_user.id if message.from_user else "Unknown ID"
    username = message.from_user.username if message.from_user.username else "No Username"
    
    details = f"""<b>sᴏᴜʀᴄᴇ ʀᴜɴɴɪɴɢ ᴏɴ {app.mention} ɪs ᴀ ᴘʀɪᴠᴀᴛᴇ sᴏᴜʀᴄᴇ ʙʏ</b> <a href="https://t.me/Devine_Network">ᴅᴇᴠɪɴᴇ ɴᴇᴛᴡᴏʀᴋ</a>.
    
<b>• ᴛʜɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ʜɪɢʜ-ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ sᴛʀᴇᴀᴍɪɴɢ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs.</b>
<b>• ɪᴛ ᴏғғᴇʀs sᴇᴀᴍʟᴇss ᴘʟᴀʏʙᴀᴄᴋ, ɪɴᴛᴜɪᴛɪᴠᴇ ᴄᴏɴᴛʀᴏʟs, ᴀɴᴅ ᴄᴏɴsɪsᴛᴇɴᴛ ᴘᴇʀғᴏʀᴍᴀɴᴄᴇ.</b>

<b><i>- ғᴏʀ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ, ᴄᴏɴᴛʀɪʙᴜᴛɪᴏɴs, ᴏʀ ᴛᴇᴄʜɴɪᴄᴀʟ sᴜᴘᴘᴏʀᴛ, ᴠɪsɪᴛ</i></b> <a href="https://t.me/devine_support">ᴅᴇᴠɪɴᴇ sᴜᴘᴘᴏʀᴛ</a>.
<b><i>ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴊᴏɪɴ</b> <a href="https://t.me/Devine_Network">ᴅᴇᴠɪɴᴇ ɴᴇᴛᴡᴏʀᴋ</i></b> <b>ғᴏʀ ғᴜʀᴛʜᴇʀ ᴜᴘᴅᴀᴛᴇs, ᴀɴᴅ ʀᴇsᴏᴜʀᴄᴇs.</b>
"""

    network = """
<b><i>sᴛᴀʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴋᴇᴇᴘ ᴛʜᴇ ᴍᴜsɪᴄ ɢᴏɪɴɢ, ᴀɴᴅ ᴇɴᴊᴏʏ ᴛʜᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ</i></b>.
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "ᴅᴇᴠɪɴᴇ ᴜᴘᴅᴀᴛᴇs", 
                    url="https://t.me/devine_updates"
                )
            ]
        ]
    )

    await message.reply_text(
        text=details.format(mention=app.mention) + network,
        disable_web_page_preview=True,
        reply_markup=buttons
    )

    message = f"""<b>{user_mention} ᴜsᴇᴅ sᴏᴜʀᴄᴇ ᴄᴏᴍᴍᴀɴᴅ.</b>

• ɪᴅᴇɴᴛɪғɪᴇʀ : {user_id}
• ʜᴀɴᴅʟᴇ : @{username}
"""
    await client.send_message(OWNER_ID, message)
