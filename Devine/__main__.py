import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import configuration
from Devine import LOGGER, app, userbot
from Devine.root.call import Devine
from Devine.misc import sudo
from Devine.programs import ALL_PROGRAMS
from Devine.utils.database import get_banned_users, get_gbanned
from configuration import filter_users

# Import redeploy command (relative import, considering the repo structure)
import sys
sys.path.append("..")  # Add the parent directory to the Python path
from redeploy import redeploy  # Now the redeploy.py can be imported

async def init():
    if (
        not configuration.STRING1
        and not configuration.STRING2
        and not configuration.STRING3
        and not configuration.STRING4
        and not configuration.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        return  # Changed from exit() to return
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            filter_users.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            filter_users.add(user_id)
    except Exception as e:
        LOGGER(__name__).error(f"Error fetching banned users: {e}")
    await app.start()
    for all_module in ALL_PROGRAMS:
        importlib.import_module("Devine.programs" + all_module)
    LOGGER("Devine.programs").info("Successfully Imported Programss...")
    await userbot.start()
    await Devine.start()
    try:
        await Devine.stream_call("https://telegra.ph//file/1df0320b93c2f3353c3e6.mp4")
    except NoActiveGroupCall:
        LOGGER("Devine").error(
            "Please turn on the video chat of your log group/channel.\n\nStopping Bot..."
        )
        return  # Changed from exit() to return
    except Exception as e:
        LOGGER("Devine").error(f"Error in streaming call: {e}")
    await Devine.decorators()
    LOGGER("Devine").info(
        "Powered by @Devine_network."
    )
    await idle()  # Keeps the bot running
    await shutdown()  # Proper shutdown sequence


async def shutdown():
    LOGGER("Devine").info("Shutting down gracefully...")
    try:
        await app.stop()
        await userbot.stop()
        LOGGER("Devine").info("Stopping AnonX Music Bot...")
    except Exception as e:
        LOGGER("Devine").error(f"Error during shutdown: {e}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
