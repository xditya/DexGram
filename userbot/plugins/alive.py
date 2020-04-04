"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**Bot Name:- Mast User Bot**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**Telethon version:- 6.9.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**Python: 3.7.3**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**Bot Made By:- @Zylern\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**"
                     "**Database Status: Databases functioning normally!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     f"**My Master**: {DEFAULTUSER}\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**[Deploy this userbot Now]**(https://github.com/Zylern/MastUserBot)\n"
                     "◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**JAI HIND🇮🇳🇮🇳 Jai Mahakaal 🙏🙏**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆")
