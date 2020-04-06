# Coded By Zylern
"""COMMAND : .aag"""

from telethon import events
from uniborg.util import admin_cmd
import asyncio

@borg.on(admin_cmd(pattern="aag ?(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 40
    

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "aag":

        await event.edit(input_str)

        animation_chars = [

            "Aag Lagi",
            "🔥",    
            "🌬💨⁠          🔥",
            "🌬 💨         🔥",
            "🌬   💨       🔥",
            "🌬    💨      🔥",
            "🌬     💨     🔥",
            "🌬      💨    🔥",
            "🌬       💨   🔥",    
            "🌬         💨 🔥",
            "🌬          💨🔥",
            "🌬             💨",
            "**Aag Bhuj Gyi** 😁",

        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 103])
