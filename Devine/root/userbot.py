from pyrogram import Client

import configuration

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="Devine1",
            api_id=configuration.API_ID,
            api_hash=configuration.API_HASH,
            session_string=str(configuration.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="Devine2",
            api_id=configuration.API_ID,
            api_hash=configuration.API_HASH,
            session_string=str(configuration.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="Devine3",
            api_id=configuration.API_ID,
            api_hash=configuration.API_HASH,
            session_string=str(configuration.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="Devine4",
            api_id=configuration.API_ID,
            api_hash=configuration.API_HASH,
            session_string=str(configuration.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="Devine5",
            api_id=configuration.API_ID,
            api_hash=configuration.API_HASH,
            session_string=str(configuration.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        if configuration.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("Devine_Network")
                await self.one.join_chat("Devine_Community")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(configuration.LOGGER_ID, "<b>ᴀssɪsᴛᴀɴᴛ 𝟷 sᴛᴀʀᴛᴇᴅ</b>")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if configuration.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("Devine_Network")
                await self.two.join_chat("Devine_community")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(configuration.LOGGER_ID, "<b>ᴀssɪsᴛᴀɴᴛ 𝟸 sᴛᴀʀᴛᴇᴅ</b>")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if configuration.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("Devine_Network")
                await self.three.join_chat("Devine_community")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(configuration.LOGGER_ID, "<b>ᴀssɪsᴛᴀɴᴛ 𝟹 sᴛᴀʀᴛᴇᴅ</b>")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if configuration.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("Devine_Network")
                await self.four.join_chat("Devine_community")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(configuration.LOGGER_ID, "<b>ᴀssɪsᴛᴀɴᴛ 𝟺 sᴛᴀʀᴛᴇᴅ</b>")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if configuration.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("Devine_Network")
                await self.five.join_chat("Devine_community")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(configuration.LOGGER_ID, "<b>ᴀssɪsᴛᴀɴᴛ 𝟻 sᴛᴀʀᴛᴇᴅ</b>")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if configuration.STRING1:
                await self.one.stop()
            if configuration.STRING2:
                await self.two.stop()
            if configuration.STRING3:
                await self.three.stop()
            if configuration.STRING4:
                await self.four.stop()
            if configuration.STRING5:
                await self.five.stop()
        except:
            pass
