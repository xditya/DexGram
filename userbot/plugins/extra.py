import asyncio, subprocess
import lyricsgenius
import time, re, io
from userbot import bot, BOTLOG, BOTLOG_CHATID, CMD_HELP, GENIUS, GENIUS_API_TOKEN
from telethon import events, functions, types
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from collections import deque
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.utils import admin_cmd

@borg.on(admin_cmd("leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I am leaving this fucking thing!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sir This is Not A Chat`')

@borg.on(outgoing=True, pattern="^.lyrics(?: |$)(.*)")
async def lyrics(lyr):
	if GApi == 'None':
		await lyr.edit(
			"`provide genius api Heroku Var first `"
		)
	try:
		args = lyr.text.split()
		artist = lyr.text.split()[1]
		snameinit = lyr.text.split(' ', 2)
		sname = snameinit[2]
	except Exception:
		await lyr.edit("` provide artist and song names `")
		return

	#Try to search for * in artist string(for multiword artist name)
	try:
		artist = artist.replace('*', ' ')
	except Exception:
		artist = lyr.text.split()[1]
		pass

	if len(args) < 3:
		await lyr.edit("`Please provide artist and song names`")

	await lyr.edit(f"`Searching lyrics for {artist} - {sname}...`")

	try:
		song = genius.search_song(sname, artist)
	except TypeError:
		song = None

	if song is None:
		await lyr.edit(f"Song **{artist} - {sname}** not found!")
		return
	if len(song.lyrics) > 4096:
			await lyr.edit("`Lyrics is too big, view the file to see it.`")
			file = open("lyrics.txt", "w+")
			file.write(f"Search query: \n{artist} - {sname}\n\n{song.lyrics}")
			file.close()
			await lyr.client.send_file(
				lyr.chat_id,
				"lyrics.txt",
				reply_to=lyr.id,
			)
			os.remove("lyrics.txt")
	else:
		await lyr.edit(f"**Search query**: \n`{artist} - {sname}`\n\n```{song.lyrics}```")
	return

@borg.on(admin_cmd(";__;$"))
#@register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)

@borg.on(admin_cmd("Oof$"))
#@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@borg.on(admin_cmd("fp$"))
#@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")
	

@borg.on(admin_cmd("moon$"))
#@register(outgoing=True, pattern="^.mmoon$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		

@borg.on(admin_cmd("source$"))
#@register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/Zylern/MastUserBot")

@borg.on(admin_cmd("readme$"))
#@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/Zylern/MastUserBot/blob/master/README.md")



@borg.on(admin_cmd("heart$"))		
#@register(outgoing=True, pattern="^.heart$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd("fap$"))
#@register(outgoing=True, pattern="^.fap$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🍆✊🏻💦"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd("myusernames$"))
#@register(outgoing=True, pattern="^.myusernames$")
async def _(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)



CMD_HELP.update({
    "leave": "Leave a Chat"
})
CMD_HELP.update({
    ";__;": "You try it!"
})
CMD_HELP.update({
    "fp": "Send face palm emoji."
})
CMD_HELP.update({
    "moon": "Bot will send a cool moon animation."
})
CMD_HELP.update({
    "clock": "Bot will send a cool clock animation."
})
CMD_HELP.update({
    "readme": "Reedme."
})
CMD_HELP.update({
    "source": "Gives the source of your userbot"
})
CMD_HELP.update({
    "myusernames": "List of Usernames owned by you."
})
CMD_HELP.update({
    "oof": "Same as ;__; but ooof"
})
CMD_HELP.update({
    "earth": "Sends Kensar Earth animation"
})
CMD_HELP.update({
    "heart": "Try and you'll get your emotions back"
})
CMD_HELP.update({
    "fap": "Faking orgasm"
})
CMD_HELP.update({
    "cry": "Show Crying Animation"
})
