from Dev import app 
import asyncio
import random
from Devine.misc import SUDOERS 
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [
    "<b>ʜᴇʏ ʙᴀʙʏ ᴋᴀʜᴀ ʜᴏ 🤗🥱</b>",
    "<b>ᴏʏᴇ sᴏ ɢʏᴇ ᴋʏᴀ ᴏɴʟɪɴᴇ ᴀᴀ 😊</b>",
    "<b>ᴠᴄ ᴄʜᴀʟᴏ ʙᴀᴛᴇɴ ᴋᴀʀᴛᴇ ʜᴀɪɴ ᴋᴜᴄʜ ᴋᴜᴄʜ 😃</b>",
    "<b>ᴋʜᴀɴᴀ ᴋʜᴀ ʟɪʏᴇ ᴊɪ..?? 🥲</b>",
    "<b>ɢʜᴀʀ ᴍᴇ sᴀʙ ᴋᴀɪsᴇ ʜᴀɪɴ ᴊɪ 🥺</b>",
    "<b>ᴘᴛᴀ ʜᴀɪ ʙᴏʜᴏᴛ ᴍɪss ᴋᴀʀ ʀᴀʜɪ ᴛʜɪ ᴀᴀᴘᴋᴏ 🤭</b>",
    "<b>ᴏʏᴇ ʜᴀʟ ᴄʜᴀʟ ᴋᴀɪsᴀ ʜᴀɪ..?? 🤨</b>",
    "<b>ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴀʀʙᴀ ᴅᴏɢᴇ..?? 🙂</b>",
    "<b>ᴀᴀᴘᴋᴀ ɴᴀᴀᴍ ᴋʏᴀ ʜᴀɪ..?? 🥲</b>",
    "<b>ɴᴀsᴛᴀ ʜᴜᴀ ᴀᴀᴘᴋᴀ..?? 😋</b>",
    "<b>ᴍᴇʀᴇ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴍᴇ ᴋɪᴅɴᴀᴘ ᴋʀ ʟᴏ 😍</b>",
    "<b>ᴀᴀᴘᴋɪ ᴘᴀʀᴛɴᴇʀ ᴀᴀᴘᴋᴏ ᴅʜᴜɴᴅ ʀᴀʜɪ ʜᴀɪɴ ᴊʟᴅɪ ᴏɴʟɪɴᴇ ᴀᴀʏɪʏᴇ 😅😅</b>",
    "<b>ᴍᴇʀᴇ sᴇ ᴅᴏsᴛɪ ᴋᴀʀᴏɢᴇ..?? 🤔</b>",
    "<b>sᴏɴᴇ ᴄʜᴀʟ ɢʏᴇ ᴋʏᴀ 🙄🙄</b>",
    "<b>ᴇᴋ sᴏɴɢ ᴘʟᴀʏ ᴋʀᴏ ɴᴀ ᴘʟsss 😕</b>",
    "<b>ᴀᴀᴘ ᴋᴀʜᴀ sᴇ ʜᴏ..?? 🙃</b>",
    "<b>ʜᴇʟʟᴏ ᴊɪ ɴᴀᴍᴀsᴛᴇ 😛</b>",
    "<b>ʜᴇʟʟᴏ ʙᴀʙʏ ᴋᴋʀᴀʜ..? 🤔</b>",
    "<b>ᴅᴏ ʏᴏᴜ ᴋɴᴏᴡ ᴡʜᴏ ɪs ᴍʏ ᴏᴡɴᴇʀ.?</b>",
    "<b>ᴄʜᴀʟᴏ ᴋᴜᴄʜ ɢᴀᴍᴇ ᴋʜᴇʟᴛᴇ ʜᴀɪɴ 🤗</b>",
    "<b>ᴀᴜʀ ʙᴀᴛᴀᴏ ᴋᴀɪsᴇ ʜᴏ ʙᴀʙʏ 😇</b>",
    "<b>ᴛᴜᴍʜᴀʀɪ ᴍᴜᴍᴍʏ ᴋʏᴀ ᴋᴀʀ ʀᴀʜɪ ʜᴀɪ 🤭</b>",
    "<b>ᴍᴇʀᴇ sᴇ ʙᴀᴀᴛ ɴᴏɪ ᴋᴀʀᴏɢᴇ 🥺🥺</b>",
    "<b>ᴏʏᴇ ᴘᴀɢʟᴀ ᴏɴʟɪɴᴇ ᴀᴀ ᴊᴀ 😶</b>",
    "<b>ᴀᴀᴊ ʜᴏʟɪᴅᴀʏ ʜᴀɪ ᴋʏᴀ sᴄʜᴏᴏʟ ᴍᴇ..?? 🤔</b>",
    "<b>ᴏʏᴇ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 😜</b>",
    "<b>sᴜɴᴏ ᴇᴋ ᴋᴀᴀᴍ ʜᴀɪ ᴛᴜᴍsᴇ 🙂</b>",
    "<b>ᴋᴏɪ sᴏɴɢ ᴘʟᴀʏ ᴋʀᴏ ɴᴀ 😪</b>",
    "<b>ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜ ☺</b>",
    "<b>ʜᴇʟʟᴏ 🙊</b>",
    "<b>sᴛᴜᴅʏ ᴄᴏᴍᴘʟᴇᴛᴇ ʜᴜᴀ?? 😺</b>",
    "<b>ʙᴏʟᴏ ɴᴀ ᴋᴜᴄʜ ʏʀʀ 🥲</b>",
    "<b>sᴏɴᴀʟɪ ᴋᴏɴ ʜᴀɪ...?? 😅</b>",
    "<b>ᴛᴜᴍʜᴀʀɪ ᴇᴋ ᴘɪᴄ ᴍɪʟʟᴇɢɪ..? 😅</b>",
    "<b>ᴍᴜᴍᴍʏ ᴀᴀ ɢᴀʏɪ ᴋʏᴀ 😆😆</b>",
    "<b>ᴀᴜʀ ʙᴀᴛᴀᴏ ʙʜᴀʙʜɪ ᴋᴀɪsɪ ʜᴀ 😉</b>",
    "<b>ɪ ʟᴏᴠᴇ ʏᴏᴜ 🙈</b>",
    "<b>ᴅᴏ ʏᴏᴜ ʟᴏᴠᴇ ᴍᴇ..? 👀</b>",
    "<b>ʀᴀᴋʜɪ ᴋᴀʙ ʙᴀɴᴅ ʀᴀʜɪ ʜᴏ.?? 🙉</b>",
    "<b>ᴇᴋ sᴏɴɢ sᴜɴᴀᴀᴜ..? 😹</b>",
    "<b>ᴏɴʟɪɴᴇ ᴀᴀ ᴊᴀ ʀᴇ sᴏɴɢ sᴜɴᴀ ʀᴀʜɪ ʜᴜ 😻</b>",
    "<b>ɪɴsᴛᴀɢʀᴀᴍ ᴄʜᴀʟᴀᴀᴛᴇ ʜᴏ..? 🙃</b>",
    "<b>ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ ᴅᴏɢᴇ ᴀᴘɴᴀ ᴛᴜᴍ..? 😕</b>",
    "<b>ᴛᴜᴍʜᴇ ᴋᴏɴ sᴀ ᴍᴜsɪᴄ sᴜɴɴᴀ ᴘᴀsᴀɴᴅ ʜᴀɪ..? 🙃</b>",
    "<b>sᴀʀᴀ ᴋᴀᴀᴍ ᴋʜᴀᴛᴀᴍ ʜᴏ ɢᴀʏᴀ ᴀᴀᴘᴋᴀ..? 🙃</b>",
    "<b>ᴋᴀʜᴀ sᴇ ʜᴏ ᴀᴀᴘ 😊</b>",
    "<b>sᴜɴᴏ ɴᴀ 🧐</b>",
    "<b>ᴍᴇʀᴀ ᴇᴋ ᴋᴀᴀᴍ ᴋᴀʀ ᴅᴏɢᴇ..?</b>",
    "<b>ʙʏ ᴛᴀᴛᴀ ᴍᴀᴛ ʙᴀᴀᴛ ᴋᴀʀɴᴀ ᴀᴀᴊ ᴋᴇ ʙᴀᴅ 😠</b>",
    "<b>ᴍᴏᴍ ᴅᴀᴅ ᴋᴀɪsᴇ ʜᴀɪɴ..? ❤</b>",
    "<b>ᴋʏᴀ ʜᴜᴀ..? 👱</b>",
    "<b>ʙᴏʜᴏᴛ ʏᴀᴀᴅ ᴀᴀ ʀᴀʜɪ ʜᴀɪ 🤧❣️</b>",
    "<b>ʙʜᴜʟ ɢʏᴇ ᴍᴜᴊʜᴇ 😏</b>",
    "<b>ᴊᴜᴛʜ ɴᴀʜɪ ʙᴏʟɴᴀ ᴄʜᴀʜɪʏᴇ 🤐</b>",
    "<b>ᴋʜᴀ ʟᴏ ʙʜᴀᴡ ᴍᴀᴛ ᴋʀᴏ ʙᴀᴀ 😒</b>",
    "<b>ᴋʏᴀ ʜᴜᴀ 😮😮</b>",
    "<b>ʜɪɪ 👀</b>",
    "<b>ᴀᴀᴘᴋᴇ ᴊᴀɪsᴀ ᴅᴏsᴛ ʜᴏ sᴀᴛʜ ᴍᴇ ғɪʀ ɢᴜᴍ ᴋɪ ʙᴀᴛ ᴋᴀ 🙈</b>",
    "<b>ᴀᴀᴊ ᴍᴀɪ sᴀᴅ ʜᴜ ☹️</b>",
    "<b>ᴍᴜᴊʜsᴇ ʙʜɪ ʙᴀᴀᴛ ᴋᴀʀ ʟᴏ ɴᴀ 🥺🥺</b>",
    "<b>ᴋʏᴀ ᴋᴀʀ ʀᴀʜᴇ ʜᴏ 👀</b>",
    "<b>ᴋʏᴀ ʜᴀʟ ᴄʜᴀʟ ʜᴀɪ 🙂</b>",
    "<b>ᴋᴀʜᴀ sᴇ ʜᴏ ᴀᴀᴘ..? 🤔</b>",
    "<b>ᴄʜᴀᴛᴛɪɴɢ ᴋᴀʀ ʟᴏ ɴᴀ.. 🥺</b>",
    "<b>ᴍᴇ ᴍᴀsᴏᴏᴍ ʜᴜ ɴᴀ 🥺🥺</b>",
    "<b>ᴋᴀʟ ᴍᴀᴊᴀ ᴀᴀʏᴀ ᴛʜᴀ ɴᴀ 🤭😅</b>",
    "<b>ɢʀᴏᴜᴘ ᴍᴇ ʙᴀᴛ ᴋʏᴜɴ ɴᴀʜɪ ᴋᴀʀᴛᴇ ʜᴏ 😕</b>",
    "<b>ᴀᴀᴘ ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ᴍᴇ ʜᴏ..? 👀</b>",
    "<b>ᴋɪᴛɴᴀ ᴄʜᴜᴘ ʀᴀʜᴛᴇ ʜᴏ ʏʀʀ 😼</b>",
    "<b>ᴀᴀᴘᴋᴏ ɢᴀɴᴀ ɢᴀɴᴇ ᴀᴀᴛᴀ ʜᴀɪ..? 😸</b>",
    "<b>ɢʜᴜᴍɴᴇ ᴄʜᴀʟᴏɢᴇ..?? 🙈</b>",
    "<b>ᴋʜᴜsʜ ʀᴀʜᴀ ᴋᴀʀᴏ ✌️🤞</b>",
    "<b>ʜᴀᴍ ᴅᴏsᴛ ʙᴀɴ sᴀᴋᴛᴇ ʜᴀɪ...? 🥰</b>",
    "<b>ᴋᴜᴄʜ ʙᴏʟ ᴋʏᴜɴ ɴᴀʜɪ ʀᴀʜᴇ ʜᴏ.. 🥺🥺</b>",
    "<b>ᴋᴜᴄʜ ᴍᴇᴍʙᴇʀs ᴀᴅᴅ ᴋᴀʀ ᴅᴏ 🥲</b>",
    "<b>sɪɴɢʟᴇ ʜᴏ ʏᴀ ᴍɪɴɢʟᴇ 😉</b>",
    "<b>ᴀᴀᴏ ᴘᴀʀᴛʏ ᴋᴀʀᴛᴇ ʜᴀɪɴ 😋🥳</b>",
    "<b>ʜᴇᴍʟᴏᴏᴏ 🧐</b>",
    "<b>ᴍᴜᴊʜᴇ ʙʜᴜʟ ɢʏᴇ ᴋʏᴀ 🥺</b>",
    "<b>ʏᴀʜᴀ ᴀᴀ ᴊᴀᴏ:- [ @InfinityGrabbers ] ᴍᴀsᴛɪ ᴋᴀʀᴇɴɢᴇ 🤭🤭</b>",
    "<b>ᴛʀᴜᴛʜ ᴀɴᴅ ᴅᴀʀᴇ ᴋʜᴇʟᴏɢᴇ..? 😊</b>",
    "<b>ᴀᴀᴊ ᴍᴜᴍᴍʏ ɴᴇ ᴅᴀᴛᴀ ʏʀʀ 🥺🥺</b>",
    "<b>ᴊᴏɪɴ ᴋᴀʀ ʟᴏ:- [ @InfinityGrabbers ] 🤗</b>",
    "<b>ᴇᴋ ᴅɪʟ ʜᴀɪ ᴇᴋ ᴅɪʟ ʜɪ ᴛᴏ ʜᴀɪ 😗😗</b>",
    "<b>ᴛᴜᴍʜᴀʀᴇ ᴅᴏsᴛ ᴋᴀʜᴀ ɢʏᴇ🥺</b>",
    "<b>ᴋᴀʜᴀ ᴋʜᴏʏᴇ ʜᴏ ᴊᴀᴀɴ 😜</b>",
    "<b>ɢᴏᴏᴅ ɴ𝟾 ᴊɪ ʙʜᴜᴛ ʀᴀᴛ ʜᴏ ɢʏɪ 🥰</b>",
]

@app.on_message(filters.command(["spam"], prefixes=["/", "."]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("<b>ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴛʜᴏsᴇ sᴍᴀʀᴛ ᴇɴᴏᴜɢʜ ᴛᴏ ᴜsᴇ ɪᴛ. Iғ ʏᴏᴜ ᴄᴀɴ’ᴛ ʜᴀɴᴅʟᴇ ɪᴛ, ᴍᴀʏʙᴇ ʏᴏᴜ sʜᴏᴜʟᴅ ʀᴇᴛʜɪɴᴋ ʏᴏᴜʀ sᴛᴀᴛᴜs.</b>")

    if message.from_user.id in SUDOERS:
        is_admin = True  
    else:
        is_admin = False
        try:
            participant = await client.get_chat_member(chat_id, message.from_user.id)
            is_admin = participant.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)
        except UserNotParticipant:
            is_admin = False

    if not is_admin:
        return await message.reply("<b>ʏᴏᴜ’ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴀʀʟɪɴɢ. ᴏɴʟʏ ᴛʜᴏsᴇ ᴡɪᴛʜ ᴀᴄᴛᴜᴀʟ ᴀᴜᴛʜᴏʀɪᴛʏ ᴄᴀɴ ᴅᴏ ᴛʜɪs.</b>")

    if message.reply_to_message and message.text:
        return await message.reply("<b>/sᴘᴀᴍ ᴊᴜsᴛ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ, sᴡᴇᴇᴛʜᴇᴀʀᴛ. ᴏʀ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ.</b>")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("<b>/sᴘᴀᴍ ᴊᴜsᴛ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ, sᴡᴇᴇᴛʜᴇᴀʀᴛ. ᴏʀ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ.</b>")
    else:
        return await message.reply("<b>/sᴘᴀᴍ ᴊᴜsᴛ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ.</b>")

    if chat_id in spam_chats:
        return await message.reply("<b>ᴏʜʜ, ᴘʟᴇᴀsᴇ ! ᴀᴛ ʟᴇᴀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴛʜᴇ ᴘʀᴏᴄᴇss ғᴏʀ ᴀ ᴍᴏᴍᴇɴᴛ.</b>")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""  # Initialize usrtxt as an empty string

    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"{usr.user.mention} "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}]({usr.mention})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except ValueError:
        pass 


@app.on_message(filters.command(["spamstop"]))
async def cancel_spam(client, message):
    if message.chat.id not in spam_chats:
        return await message.reply("<b>ᴄᴜʀʀᴇɴᴛʟʏ, ɪ'ᴍ ɴᴏᴛ sᴘᴀᴍᴍɪɴɢ, ᴅᴀʀʟɪɴɢ...</b>")
    
    if message.from_user.id in SUDOERS:
        spam_chats.remove(message.chat.id)  
        return await message.reply("<b>ᴀʜʜ, ғᴏʀ ʜᴇᴀᴠᴇɴ's sᴀᴋᴇ, ɪᴛ's sᴛᴏᴘᴘᴇᴅ.</b>")
    
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
        is_admin = participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        )
    except UserNotParticipant:
        is_admin = False

    if not is_admin:
        return await message.reply("<b>ʏᴏᴜ’ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴀʀʟɪɴɢ. ᴏɴʟʏ ᴛʜᴏsᴇ ᴡɪᴛʜ ᴀᴄᴛᴜᴀʟ ᴀᴜᴛʜᴏʀɪᴛʏ ᴄᴀɴ ᴅᴏ ᴛʜɪs.</b>")
    
    try:
        spam_chats.remove(message.chat.id)
    except ValueError:
        pass  
    return await message.reply("<b>ᴀʜʜ, ғᴏʀ ʜᴇᴀᴠᴇɴ's sᴀᴋᴇ, ɪᴛ's sᴛᴏᴘᴘᴇᴅ.</b>")
