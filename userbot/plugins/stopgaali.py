#plugin by @Zylern

from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("stopgaali ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Gaali")
        await asyncio.sleep(0.4)
        await event.edit("Mat")
        await asyncio.sleep(0.4)
        await event.edit("Do")
        await asyncio.sleep(0.4)
        await event.edit("Gaali")
        await asyncio.sleep(0.4)
        await event.edit("Mat")
        await asyncio.sleep(0.4)
        await event.edit("Lo")
        await asyncio.sleep(0.4)
        await event.edit("Itne")
        await asyncio.sleep(0.4)
        await event.edit("Ghade")
        await asyncio.sleep(0.4)
        await event.edit("Khod")
        await asyncio.sleep(0.4)
        await event.edit("Dunga")
        await asyncio.sleep(0.4)
        await event.edit("Agle")
        await asyncio.sleep(0.4)
        await event.edit("Janam")
        await asyncio.sleep(0.4)
        await event.edit("Me")
        await asyncio.sleep(0.4)
        await event.edit("Tera")
        await asyncio.sleep(0.4)
        await event.edit("Baap")
        await asyncio.sleep(0.4)
        await event.edit("Bankar")
        await asyncio.sleep(0.4)
        await event.edit("Teri")
        await asyncio.sleep(0.4)
        await event.edit("Maa")
        await asyncio.sleep(0.4)
        await event.edit("Chod")
        await asyncio.sleep(0.4)
        await event.edit("Dunga")
        await asyncio.sleep(0.4)
        
        await event.edit("**Gaali Mat Do Gaali Mat Lo Itne Ghade Khod Dunga Agle Janam Me Tera Baap Bankar Teri Maa Chod Dunga.**")
