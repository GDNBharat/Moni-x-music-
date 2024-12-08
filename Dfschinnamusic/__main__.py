import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Dfschinnamusic import LOGGER, app, userbot
from Dfschinnamusic.core.call import Dfs
from Dfschinnamusic.misc import sudo
from Dfschinnamusic.plugins import ALL_MODULES
from Dfschinnamusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Dfschinnamusic.plugins" + all_module)
    LOGGER("Dfschinnamusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Dfs.start()
    try:
        await Dfs.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Dfschinnamusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Dfs.decorators()
    LOGGER("Dfschinnamusic").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝐂𝐡𝐢𝐧𝐧𝐚 ♨️\n╚═════ஜ۩۞۩ஜ════╝") 
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Dfschinnamusic").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝐂𝐡𝐢𝐧𝐧𝐚 ♨️\n╚═════ஜ۩۞۩ஜ════╝")
        ")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
