# Coded By Zylern
"""
Show different synonyms of nope
Syntax: .loveyou

"""
from telethon import events
import os
import sys
import random, re
import asyncio
from uniborg.util import admin_cmd
from telethon import events


@borg.on(admin_cmd(pattern="loveyou ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    x=(random.randrange(1,14)) 
    if (x==1):
      await event.edit("┊┊╭━╮┊┊┊┊┊┊┊┊┊┊┊\n━━╋━╯┊┊┊┊┊┊┊┊┊┊┊\n┊┊┃┊╭━┳╮╭┓┊╭╮╭━╮\n╭━╋━╋━╯┣╯┃┊┃╰╋━╯\n╰━╯┊╰━━╯┊╰━┛┊╰━━")
    if (x==2):
      await event.edit("╔══╗\n╚╗╔╝ ╔╗╔═╦╦╦═╗ ╔╗╔╗\n╔╝╚╗ ║╚╣║║║║╩╣ ║╚╝║\n╚══╝ ╚═╩═╩═╩═╝ ╚══╝")
    if (x==3):
      await event.edit("┏┓┏┓┏━┳┳┳━┓┏┳┳━┳┳┓\n┃┃┃┗┫┃┃┃┃━┫┣┓┃┃┃┃┃\n┗┛┗━┻━┻━┻━┛┗━┻━┻━┛")
    if (x==4):
      await event.edit("┈╱╱╱╱╱╲╲╲┈╱╱╲╲╲╲\n┈▏▕╭▅╭▅▕▕╭▏▅╮▅╮▕╮\n┈▏╱▔▔╮▔▕▕╰▏▔╭▔▔▕╯\n▕╱╲╰━━╯╱╲▏╲╰━━╯╱\n┈┈╭▔▔▔▔╲┈┈╱▔▔▔▔╮\n┈┈┃▏┊┊▕╲╲╱╱▏┊┊▕┃\n┈┈╰▏▂▂▕┈╰╯┈▏▂▂▕╯\n┈┈▕▂▏▕▂▏┈┈▕▂▏▕▂▏")
    if (x==5):
      await event.edit("┳┻┳┻╭━━━━╮╱▔▔▔╲\n┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\nLove You Forever,,,,")
    if (x==6):
      await event.edit(". O * O         O *  O\nO          * O *           O\n O                           O\n   * O                 O *\n            *   O   *\n•✤─█▄◯╲╱☰─✤•")
    if (x==7):
      await event.edit("╔══╗♥\n╚╗╔╝♥\n╔╝╚╗♥\n╚══╝♥\n╔╗ ♥ღ♥ღ♥ღ♥\n║║╔═╦╦╦╔╗\n║╚╣║║║║╔╣\n╚═╩═╩═╩═╝\n╔╗╔╗♥\n║║║║♥\n║╚╝║♥\n╚══╝♥")
    if (x==8):
      await event.edit(".﹎ ┈ ┈ ┈ ﹎\n﹎┈   ●     O .﹎ ﹎\n┈ ┈ /█\/▓\ ﹎ ┈\n▅▆▇█████▇▆▅")
    if (x==9):
      await event.edit("╔══╗╔╗  ♡\n╚╗╔╝║║╔═╦╦╦╔╗\n╔╝╚╗║╚╣║║║║╔╣\n╚══╝╚═╩═╩═╩═╝\nஜ۩۞۩ஜ YOU ஜ۩۞۩ஜ")
    if (x==10):
      await event.edit("╔===╗   WILL\n╚╗ ╔╝   NEVER\n╔╝ ╚╗   STOP\n╚===╝   ♡ING YOU")
    if (x==11):
      await event.edit("┏╗ ┏╗\n║┃ ║┃╔━╦╦┳═╗\n║┃ ┃╚┫║┃┃┃╩┫\n┗╝ ╚━╩═┻━╩━╝\n┓╔┓┏\n║╚┛┣═╦┳╗\n┗╗┏╣┃┃║┃\n   ┗╝┗═┻═╝")
    if (x==12):
      await event.edit("(¨·.·´¨)  I\n  ·.(¨·.·´¨)Love\n         ·.¸.·´ You")
    if (x==13):
      await event.edit("┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n┈┈┈◢▇◣┈┈◢▇◣┈┈┈\n┈┈┈▇▇▇◣◢▇▇▇┈┈┈\n┈┈┈◥▇▇▇▇▇▇◤┈┈┈\n┈┈┈┈◥▇▇▇▇◤┈┈┈┈\n┈┈┈┈┈◥▇▇◤┈┈┈┈┈\n┈┈┈┈┈┈◥◤┈┈┈┈┈┈\n                 I Love You ❤ ")