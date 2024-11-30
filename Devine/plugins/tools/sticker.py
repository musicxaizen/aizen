import base64
import httpx
import os
from pyrogram import filters
from configuration import BOT_USERNAME
from Devine import app devine
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


######### sticker id

@devine.on_message(filters.command("st"))
def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            client.send_sticker(message.chat.id, sticker=sticker_id)
        except Exception as e:
            message.reply_text(f"Error: {e}")
    else:
        message.reply_text("Please provide a sticker ID after /st command.")


#---------

from uuid import uuid4
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram.raw

@devine.on_message(filters.command("packkang"))
async def _packkang(devine, message):
    txt = await message.reply_text("**Processing...**")
    
    # Check if the message is a reply
    if not message.reply_to_message:
        await txt.edit("Please reply to a message containing a sticker.")
        return
    
    # Check if the replied message contains a non-animated sticker
    if not message.reply_to_message.sticker:
        await txt.edit("Please reply to a sticker.")
        return
    
    if message.reply_to_message.sticker.is_animated or message.reply_to_message.sticker.is_video:
        await txt.edit("Please reply to a non-animated sticker.")
        return
    
    # Determine the pack name
    if len(message.command) < 2:
        pack_name = f"{message.from_user.first_name}_sticker_pack_by_{devine.me.username}"
    else:
        pack_name = message.text.split(maxsplit=1)[1]
    
    short_name = message.reply_to_message.sticker.set_name
    try:
        # Retrieve the sticker set
        stickers = await devine.invoke(
            pyrogram.raw.functions.messages.GetStickerSet(
                stickerset=pyrogram.raw.types.InputStickerSetShortName(short_name=short_name),
                hash=0
            )
        )
    except Exception as e:
        await txt.edit(f"Failed to retrieve the sticker set: {str(e)}")
        return

    shits = stickers.documents
    sticks = []
    
    for sticker in shits:
        try:
            # Prepare the sticker for the new pack
            document = pyrogram.raw.types.InputDocument(
                id=sticker.id,
                access_hash=sticker.access_hash,
                file_reference=sticker.file_reference
            )
            emoji = sticker.attributes[1].alt if len(sticker.attributes) > 1 else "✨"
            
            sticks.append(
                pyrogram.raw.types.InputStickerSetItem(
                    document=document,
                    emoji=emoji
                )
            )
        except Exception as e:
            await txt.edit(f"Error preparing stickers: {str(e)}")
            return
    
    try:
        # Create a unique short name for the sticker pack
        short_name = f"sticker_pack_{str(uuid4()).replace('-', '')}_by_{devine.me.username}"
        user_id = await devine.resolve_peer(message.from_user.id)
        
        # Create the new sticker set
        await devine.invoke(
            pyrogram.raw.functions.stickers.CreateStickerSet(
                user_id=user_id,
                title=pack_name,
                short_name=short_name,
                stickers=sticks
            )
        )
        
        # Send the link to the new sticker pack
        await txt.edit(
            f"**Your sticker pack has been created!**\n"
            f"**Total stickers:** {len(sticks)}",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Pack Link", url=f"http://t.me/addstickers/{short_name}")]]
            )
        )
    except Exception as e:
        await txt.edit(f"Error creating sticker pack: {str(e)}")

@devine.on_message(filters.command(["stickerid","stid"]))
async def sticker_id(devine: devine, msg):
    if not msg.reply_to_message:
        await msg.reply_text("Reply to a sticker")        
    elif not msg.reply_to_message.sticker:
        await msg.reply_text("Reply to a sticker")        
    st_in = msg.reply_to_message.sticker
    await msg.reply_text(f"""
** sᴛɪᴄᴋᴇʀ ɪᴅ **: `{st_in.file_id}`\n
""")
