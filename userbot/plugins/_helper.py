from userbot.Config import Config
import asyncio

import requests
from telethon import functions

from userbot import ALIVE_NAME, CMD_LIST, SUDO_LIST
from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(allow_sudo=True, pattern="help ?(.*)"))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = Config.BOT_USERNAME
    input_str = event.pattern_match.group(1)
    try:
        if not input_str == "":
            if input_str in CMD_HELP:
                await eor(event, str(CMD_HELP[args]))
    except:
        pass
    if tgbotusername is not None:
        results = await event.client.inline_query(tgbotusername, "REBELBOT_help")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await eor(event, "**⚠️ ERROR !!** \nPlease Re-Check BOT_TOKEN & BOT_USERNAME on Heroku.")
