from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("gang ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Everybody")
        await asyncio.sleep(0.3)
        await event.edit("is")
        await asyncio.sleep(0.2)
        await event.edit("Gangster")
        await asyncio.sleep(0.5)
        await event.edit("Until ")
        await asyncio.sleep(0.2)
        await event.edit("I")
        await asyncio.sleep(0.3)
        await event.edit("ArrivE")
        await asyncio.sleep(0.3)
        await event.edit("🔥🔥🔥")
        await asyncio.sleep(0.3)
        await event.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥🔥🔥")
