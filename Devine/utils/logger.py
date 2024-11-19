from pyrogram.enums import ParseMode

from Dev import app
from Devine.utils.database import is_on_off
from configuration import LOGGER_ID

EXTRA = -1002157851716

async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>ᴍᴜsɪᴄ ʀᴇᴄᴏʀᴅs</b>

<b>ɪɴǫᴜɪʀʏ ⌯ </b>{message.text.split(None, 1)[1]}
<b>sᴏᴜʀᴄᴇ ⌯ </b>{streamtype}

<b>ᴀʙᴏᴜᴛ ᴄʜᴀᴛ - </b> 

<b>ᴅᴇsɪɢɴᴀᴛɪᴏɴ ⌯ </b> {message.chat.title}
<b>ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ </b> <code>{message.chat.id}</code>
<b>ᴄʜᴀᴛ ʜᴀɴᴅʟᴇ ⌯ </b>{message.chat.username}.t.me

<b>ᴜsᴇʀ ᴅᴀᴛᴀ - </b>

<b>ɴᴀᴍᴇ ⌯ </b>{message.from_user.mention}
<b>ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ </b><code>{message.from_user.id}</code>
<b>ʜᴀɴᴅʟᴇ ⌯ </b>{message.from_user.username}.t.me"""

        for chat_id in [LOGGER_ID, EXTRA]:
            if message.chat.id != chat_id:
                try:
                    await app.send_message(
                        chat_id=chat_id,
                        text=logger_text,
                        parse_mode=ParseMode.HTML,
                        disable_web_page_preview=True,
                    )
                except Exception as e:
                    print(f"Failed to send log to {chat_id}: {e}")
        return
