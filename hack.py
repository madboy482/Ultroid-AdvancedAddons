# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available
• `{i}hack`
    Do a Prank With Replied user.
"""
from telethon import events
import asyncio
import os
import sys
import random
from . import *

@ultroid_cmd(pattern="hack")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.7
    animation_ttl = range(0, 11)
    xx = await eor(event, "**Installing...**")
    animation_chars = [
            "**Installing Files To Hacked Private Server...**",
             "**Target Selected.**",
              "`Installing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
               "`Installing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "`Installing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
                 "`lnstallig... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                  "`Installing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                   "`Installing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
                    "`Installing... 84%\n█████████████████████▒▒▒▒ `",
                     "`Installing... 100%\n████████Installed██████████ `",
                      "**Target files Uploading...\n\nDirecting To Remote  server to hack...**"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await xx.edit(animation_chars[i % 11])
    await asyncio.sleep(2)
    animation_interval = 0.6
    animation_ttl = range(0,14)
    await xx.edit("**Connecting nd getting combined token from my.telegram.org**")
    await asyncio.sleep(1)
    animation_chars = [
            "`root@anon:~#` ",
             "`root@anon:~# ls`",
              "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~#`",
               "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...`",
                "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# `",
                 "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py`",
                  "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...`",
                   "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...`",
                    "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami`",
                     "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user`",
                      "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...`",
                       "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...`",
                        "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected in ghost ...`\n\n**All Done!**",
                         "`root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nAuto CMD deployed ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected  in ghost ...`\n\n**All Done!**\n**Installing Token!**\n**Token= DJ65gulO90P90nlkm65dRfc8I**",]
    for i in animation_ttl:  
        await asyncio.sleep(animation_interval)
        await xx.edit(animation_chars[i % 14])
    await asyncio.sleep(2)
    await xx.edit("**Starting telegram Hack**")
    await asyncio.sleep(1)
    await xx.edit("`Hacking... 0% Completed✅\nTERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (1.3) kB`")#credit to kraken,sawan
    await asyncio.sleep(2)
    await xx.edit(" `Hacking... 4% Completed✅\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packages`")
    await asyncio.sleep(1)
    await xx.edit("`hacking.....6% Completed✅\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packages from target account chat...\n lding chat tg-bot bruteforce finished.!`")
    await asyncio.sleep(1)
    await xx.edit("`hacking.....8% Completed✅\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packagesfrom target account chat...\n lding chat tg-bot bruteforce finished.!\n Creating PDF of chat`")
    await asyncio.sleep(1)
    await xx.edit("`hacking....15% Completed✅\n Terminal:Chat history from telegram exporting to private database.\n Terminal 874379gvrfghhuu5tlotruhi5rbh Installing....`")
    await asyncio.sleep(1)
    await xx.edit("`hacking....24% Completed✅\n TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packages from target account chat...\n lding chat tg-bot bruteforce finished.!\nerminal:Chat history from telegram being exported to private database.\n Terminal 874379gvrfghhuu5tlotruhi5rbh Installed!!\n Creating data into PDF`")
    await asyncio.sleep(1)
    await xx.edit("`hacking....32% Completed✅\n Looking for use history \n Downloading-telegram -id prtggtgf . gfr (12.99 mb)\n Collecting data, **!!!Starting imprute attack to user account!!!**\n Chat history from telegram being exported to private database.\n Terminal 874379gvrfghhuu5tlotruhi5rbh Installed!!\n Created data into PDF\nDownload successful Bruteforce-Telegram-0.1.tar.gz (1.3)`")
    await asyncio.sleep(1)
    await xx.edit("hacking....38% Completed✅\n\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e`")
    await asyncio.sleep(1)
    await xx.edit("`hacking....52% Completed✅\nExterting data from telegram private server\nDone with status 36748hdeg \n Checking for more data in device...`")
    await asyncio.sleep(2)
    await xx.edit("`hacking....60% Completed✅\nMore data found in target device...\nPreparing to download data...\n Process started with status 7y75hsgdt365ege56es \n Status changed to up!`")
    await asyncio.sleep(1)
    await xx.edit("`hacking....73% Completed✅\n Downloading data from device...\n Process completed with status 884hfhjh\nDownloading-0.1.tar.gz (9.3 kB)\nCollecting Data Packages from target...\n lding chat tg-bot bruteforce finished\n Creating PDF of chat`")
    await asyncio.sleep(1)
    await xx.edit("`hacking...88% Completed✅\nAll data from telegram private server downloaded✅✅\nTerminal download sucessfull--with status jh3233fdg66y yr4vv.irh\n Data collected from tg-bot\nTERMINAL:\n Bruteforce-Telegram-0.1.tar.gz (1.3)downloaded`")
    await asyncio.sleep(.5)
    await xx.edit("`100%\n█████████HACKED███████████ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Packages\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): Finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: `")
    await asyncio.sleep(2)
    await xx.edit("**Account hacked\n Collecting all data\n Converting data into PDF......**")
    await asyncio.sleep(1)
    x=(random.randrange(1,5)) 
    if x==1:
        await xx.edit("__PDF created click link below to download data\n\n😂 Don't worry, only I can open this 😎😎.. If u don't Believe try to download__ 🙂\n\n**https://drive.google.com/file/d/1EHJSkt64RZEw7a2h8xkRqZSv_4dWhB02/view?usp=sharing**")
    if x==2:
        await xx.edit("__PDF created click link below to download data\n\n😂 Don't worry, only I can open this 😎😎.. If u don't Believe try to download__ 🙂\n\n**https://drive.google.com/file/d/1YaUfNVrHU7zSolTuFN3HyHJuTWQtdL2r/view?usp=sharing**")
    if x==3:
        await xx.edit("__PDF created click link below to download data\n\n😂 Don't worry, only I can open this 😎😎.. If u don't Believe try to download__ 🙂\n\n**https://drive.google.com/file/d/1o2wXirqy1RZqnUMgsoM8qX4j4iyse26X/view?usp=sharing**")
    if x==4:
        await xx.edit("__PDF created click link below to download data\n\n😂 Don't worry, only I can open this 😎😎.. If u don't Believe try to download__ 🙂\n\n**https://drive.google.com/file/d/15-zZVyEkCFA14mFfD-2DKN-by1YOWf49/view?usp=sharing**")
    if x==5:
        await xx.edit("__PDF created click link below to download data\n\n😂 Don't worry, only I can open this 😎😎.. If u don't Believe try to download__ 🙂\n\n**https://drive.google.com/file/d/1hPUfr27UtU0XjtC20lXjY9G3D9jR5imj/view?usp=sharing**")
 
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
