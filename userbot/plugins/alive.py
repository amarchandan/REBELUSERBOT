# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) 
# Made by @REBEL_IS_OP...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in REBEL Userbot by @REBEL_IS_OP

import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, REBELversion
from REBELBOT.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for ÂÝŮ$HópBØȚ

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

REBEL = bot.uid

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/9cf4ea6de5a3b3bb44dd8.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥ℝ𝔼𝔹𝔼𝕃𝔹𝕆𝕋 𝕀𝕊 𝔸𝕃𝕀𝕍𝔼🔥🔥**__\n"

pm_caption += "🛡️𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡🛡️ : `1.15.0` \n"

pm_caption += f"😈𝗥𝗘𝗕𝗘𝗟𝗕𝗢𝗧😈 : `{REBELversion}`\n"

pm_caption += f"😱𝗦𝗨𝗗𝗢😱            : `{sudou}`\n"

pm_caption += "😇𝗖𝗛𝗔𝗡𝗡𝗘𝗟😇️   : [ᴊᴏɪɴ](https://t.me/REBELBOT_SUPPORT)\n"

pm_caption += "😎𝗖𝗥𝗘𝗔𝗧𝗢𝗥😎    : [𝗥𝗘𝗕𝗘𝗟](https://t.me/REBEL_IS_OP)\n"

pm_caption += "🤩𝗦𝗨𝗣𝗣𝗢𝗥𝗧𝗘𝗥🤩    :[ⓃⒾⓈⒽⓊ](https://t.me/nishuop5)\n"

pm_caption += "      [🔥𝗥𝗘𝗣𝗢🔥](https://github.com/REBEL75/REBELSBOT) 🔹 [📜𝗟𝗶𝗰𝗲𝗻𝘀𝗲📜](https://github.com/REBEL75/REBELSBOT/blob/main/LICENSE)\n"

pm_caption += "      [𝑹𝑶𝒀𝑨𝑳 𝑶𝑾𝑵𝑬𝑹][[{DEFAULTUSER}](tg://user?id={REBEL})]

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file1)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file2)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file3)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
