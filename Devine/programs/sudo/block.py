from pyrogram import filters
from pyrogram.types import Message

from Dev import app
from Devine.misc import SUDOERS
from Devine.utils.database import add_gban_user, remove_gban_user
from Devine.utils.decorators.language import language
from Devine.utils.extraction import extract_user
from configuration import filter_users, BOT_ID, OWNER_ID


@app.on_message(filters.command(["block"]) & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴜsᴇʀ ɪᴅ ғᴏʀ ʙʟᴏᴄᴋ ᴛʜᴇᴍ.")
    user = await extract_user(message)
    if user.id == BOT_ID:
        return await message.reply_text("ᴡʜʏ sʜᴏᴜʟᴅ ɪ ʙʟᴏᴄᴋ ᴍʏsᴇʟғ?")
    if user.id == OWNER_ID:
        return await message.reply_text("ᴀʀᴇ ʏᴏᴜ sᴇʀɪᴏᴜs? ʜᴏᴡ ᴄᴀɴ ɪ ʙʟᴏᴄᴋ ᴍʏ ʟᴏʀᴅ?")
    if user.id in filter_users:
        return await message.reply_text(f"{user.mention} ɪs ᴀʟʀᴇᴀᴅʏ ʙʟᴏᴄᴋᴇᴅ.")
    await add_gban_user(user.id)
    filter_users.add(user.id)
    await message.reply_text(f"{user.mention} ʜᴀs ʙᴇᴇɴ ʙʟᴏᴄᴋᴇᴅ.")


@app.on_message(filters.command(["unblock"]) & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴜsᴇʀ ɪᴅ ғᴏʀ ʙʟᴏᴄᴋ ᴛʜᴇᴍ.")
    user = await extract_user(message)
    if user.id not in filter_users:
        return await message.reply_text(f"{user.mention} ɪs ɴᴏᴛ ʙʟᴏᴄᴋᴇᴅ.")
    await remove_gban_user(user.id)
    filter_users.remove(user.id)
    await message.reply_text(f"{user.mention} ʜᴀs ʙᴇᴇɴ ᴜɴʙʟᴏᴄᴋᴇᴅ.")


@app.on_message(filters.command(["blocked", "blockedusers", "blusers"]) & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not filter_users:
        return await message.reply_text("ɴᴏ ᴜsᴇʀs ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ʙʟᴏᴄᴋᴇᴅ.")
    mystic = await message.reply_text("ᴀᴄᴄᴇssɪɴɢ ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs ᴅᴇᴛᴀɪʟs...")
    msg = "<b>ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs ʟɪsᴛ:</b>\n\n"
    count = 0
    for users in filter_users:
        try:
            user = await app.get_users(users)
            user = user.first_name if not user.mention else user.mention
            count += 1
        except:
            continue
        msg += f"{count}‣ {user}\n"
    if count == 0:
        return await mystic.edit_text("ɴᴏ ᴜsᴇʀs ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ʙʟᴏᴄᴋᴇᴅ.")
    else:
        return await mystic.edit_text(msg)
