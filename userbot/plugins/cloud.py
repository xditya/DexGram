# Coded by Zylern
"""Emoji

Available Commands:

.cloud
.tcloud

"""

from telethon import events
from collections import deque
from userbot.utils import admin_cmd
import asyncio

@borg.on(admin_cmd("cloud$"))
#@register(outgoing=True, pattern="^.cloud$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("☁️🌩⛈🌧🌨🌦🌥⛅🌤☀️"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "tcloud":

        await event.edit(input_str)

        animation_chars = [

            "☁️️",
            "🌩",    
            "⛈",
            "🌧",
            "🌨",
            "🌦",
            "🌥",
            "⛅",
            "🌤",
            "☀",    
            "☁️️",
            "🌩",    
            "⛈",
            "🌧",
            "🌨",
            "🌦",
            "🌥",
            "⛅",
            "🌤",
            "☀",    
            "☁️️",
            "🌩",    
            "⛈",
            "🌧",
            "🌨",
            "🌦",
            "🌥",
            "⛅",
            "🌤",
            "☀",    
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])

