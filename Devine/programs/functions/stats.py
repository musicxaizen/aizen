import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid, MessageNotModified
from pyrogram.types import Message

import configuration
from Dev import app
from Devine.root.userbot import assistants
from Devine.misc import SUDOERS, mongodb
from Devine.programs import ALL_PROGRAMS
from Devine.utils.database import get_served_chats, get_served_users, get_sudoers
from Devine.utils.decorators.language import language, languageCB
from Devine.utils.inline.stats import back_stats_buttons, stats_buttons
from configuration import filter_users
from pytgcalls.__version__ import __version__ as pytgver  # Ensure this import is present

@app.on_message(filters.command(["stats"]) & filters.group & ~filter_users)
@language
async def stats_global(client, message: Message, _):
    if message.from_user.id not in SUDOERS:
        return  # Ignore message if user is not in SUDOERS
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    await message.reply_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )

@app.on_callback_query(filters.regex("stats_back") & ~filter_users)
@languageCB
async def home_stats(client, CallbackQuery, _):
    upl = stats_buttons(_, True if CallbackQuery.from_user.id in SUDOERS else False)
    try:
        if CallbackQuery.message.text != _["gstats_2"].format(app.mention):  # Ensure text is different before editing
            await CallbackQuery.edit_message_text(
                text=_["gstats_2"].format(app.mention),
                reply_markup=upl,
            )
    except MessageNotModified:
        print("Message was not modified because the content was identical.")

@app.on_callback_query(filters.regex("TopOverall") & ~filter_users)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_3"].format(
        app.mention,
        len(assistants),
        len(filter_users),
        served_chats,
        served_users,
        len(ALL_PROGRAMS),
        len(SUDOERS),
        configuration.AUTO_LEAVING_ASSISTANT,
        configuration.DURATION_LIMIT_MIN,
    )
    await CallbackQuery.edit_message_text(text, reply_markup=upl)

@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def bot_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer(_["gstats_4"], show_alert=True)
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    p_root = psutil.cpu_count(logical=False)
    t_root = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    used = hdd.used / (1024.0**3)
    free = hdd.free / (1024.0**3)
    call = await mongodb.command("dbstats")
    datasize = call["dataSize"] / 1024
    storage = call["storageSize"] / 1024
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_5"].format(
        app.mention,
        len(ALL_PROGRAMS),
        platform.system(),
        ram,
        p_root,
        t_root,
        cpu_freq,
        pyver.split()[0],
        pyrover,
        pytgver,  # Ensure this variable is available
        str(total)[:4],
        str(used)[:4],
        str(free)[:4],
        served_chats,
        served_users,
        len(filter_users),
        len(await get_sudoers()),
        str(datasize)[:6],
        storage,
        call["collections"],
        call["objects"],
    )
    try:
        await CallbackQuery.edit_message_text(text, reply_markup=upl)
    except MessageNotModified:
        print("Attempted to edit with identical content, skipping.")
