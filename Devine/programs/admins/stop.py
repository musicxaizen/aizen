from pyrogram import filters
from pyrogram.types import Message

from Dev import app
from Devine.root.call import Devine
from Devine.utils.database import set_loop
from Devine.utils.decorators import AdminRightsCheck
from Devine.utils.inline import close_markup
from configuration import filter_users


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~filter_users
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Devine.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
