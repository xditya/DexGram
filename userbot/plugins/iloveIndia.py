# Coded by @Zylern
"""Plugin for userbot type `.iloveindia`
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="iloveindia ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("सारे जहाँ से अच्छा हिन्दोस्तान हमारा")
        await asyncio.sleep(2)
        await event.edit("हम बुलबुलें है इस की, यह गुलसितां हमारा")
        await asyncio.sleep(2)
        await event.edit("घुर्बत में हों अगर हम, रहता है दिल वतन में")
        await asyncio.sleep(3)
        await event.edit("समझो वहीं हमें भी, दिल हैं जहाँ हमारा")
        await asyncio.sleep(3)
        await event.edit("परबत वोह सब से ऊँचा, हमसाया आसमान का")
        await asyncio.sleep(3)
        await event.edit("वोह संतरी हमारा, वोह पस्बन हमारा")
        await asyncio.sleep(2)
        await event.edit("गोदी में खेलती हैं इस की हजारों नदिया")
        await asyncio.sleep(1)
        await event.edit("गुलशन है जिन के दम से, रश्क-ऐ-जनन हमारा")
        await asyncio.sleep(3)
        await event.edit("आये अब, रूद, गंगा, वोह दिन में यद तुझको")
        await asyncio.sleep(4)
        await event.edit("उतरा तेरे किनारे, जब कारवां हमारा")
        await asyncio.sleep(3)
        await event.edit("मजहब नहीं सिखाता आपस में बयर रखना")
        await asyncio.sleep(3)
        await event.edit("हिन्दवी है हम, वतन है हिन्दोस्तान हमारा")
        await asyncio.sleep(2)
        await event.edit("यूनान-ओ-मिस्र-ओ-रोमा, सब मिट गए जहाँ से")
        await asyncio.sleep(3)
        await event.edit("अब तक मगर है बाकी, नम-ओ-निशान हमारा")
        await asyncio.sleep(2)
        await event.edit("कुछ बात है कह हस्ती, मिटटी नहीं हमारी")
        await asyncio.sleep(3)
        await event.edit("सदियों रहा है दुश्मन, दौर-ऐ-ज़मान हमारा")
        await asyncio.sleep(3)
        await event.edit("इकबाल कोई महरम, अपना नहीं जहाँ में")
        await asyncio.sleep(2)
        await event.edit("मालूम क्या किसी को, दर्द-ऐ-निहां हमारा")
        await asyncio.sleep(2)
        await event.edit("#JaiHind 🇮🇳🇮🇳 #VandeMatram")
