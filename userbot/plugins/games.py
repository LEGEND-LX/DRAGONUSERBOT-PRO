# Made by @Pro_Userboy for @LegendBot_Pros
# Now in LegendBot
# Thanks to LegendBot

import asyncio

from telethon import events

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, sudo_cmd


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.2
    animation_ttl = range(0, 14)
    input_str = event.pattern_match.group(1)
    if input_str == "game":
        await event.edit(input_str)
        animation_chars = [
            "**Welcome To LegendBot Repo Game**",
            "**Click The Gift As Fast As Possible**",
            "**Game Starts in 3**",
            "**Game Starts in 2**",
            "**Game Starts in 1**",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆[🎁](https://github.com/PROBOY-OP/LegendBot)🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆[🎁](https://github.com/PROBOY-OP/LegendBot)🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇[🎁](https://github.com/PROBOY-OP/LegendBot)🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆[🎁](https://github.com/PROBOY-OP/LegendBot)🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n[🎁](https://github.com/PROBOY-OP/LegendBot)🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇[🎁](https://PROBOY-OP/LegendBot)\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇",
            "**Game Over**",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 14])


@bot.on(admin_cmd(pattern="xogame$", outgoing=True))
@bot.on(sudo_cmd(pattern="xogame$", allow_sudo=True))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


CmdHelp("games").add_command(
    "xogame", None, "Lets play a game bruh. X-O Game iz here🔥"
).add()
