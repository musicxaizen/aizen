from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import configuration

from ..logging import LOGGER


class Devine(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="Devine",
            api_id=configuration.API_ID,
            api_hash=configuration.API_HASH,
            bot_token=configuration.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=configuration.LOGGER_ID,
                text=f"<b>{self.mention} ɪs ᴀʟɪᴠᴇ <a href='https://envs.sh/KZQ.jpg' target='_blank'>✨</a></b>\n\n"
                         f"<b>• ʙᴏᴛ ᴠᴇʀsɪᴏɴ :</b> <code>𝟸.𝟷 ʀx</code>\n"
                         f"<b>• ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :</b> <code>𝟹.𝟷𝟶.𝟷𝟷</code>\n"
                         f"<b>• ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :</b> <code>𝟸.𝟶.𝟷𝟶𝟼</code>"
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(configuration.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            exit()
        LOGGER(__name__).info(f"Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
