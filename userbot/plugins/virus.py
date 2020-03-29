"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "hack":

        await event.edit(input_str)

        animation_chars = [
        
            "`Injecting this nibba Corona...`",
            "`Target Selected.`",
            "`Injecting... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injecting... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injecting... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Injecting... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injecting... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injecting... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injecting... 84%\n█████████████████████▒▒▒▒ `",
            "`Injecting... 100%\n█████████Injected Corona███████████ `",
            "`Targeted user Injected...\n\nPay 69$ To` @MisterClay `Or send nudes of female Homo Sapiens To Remove Corona Virus, or you will die in 69 mins`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
