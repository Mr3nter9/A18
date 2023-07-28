#module

import requests , random
from time import sleep
from telethon.sync import TelegramClient , events
from telethon.tl.functions.users import GetFullUserRequest
import os

#factions

id='5229914714'
token='6183317549:AAGB5jAoTSGSc0M0Y_8WR7kEa7oYbyjshM0'
led=TelegramClient('Dex_Tsh', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
led.start()
uss='qwertyuioplkjhgfdsazxcvbnm1234567890'
rr='qwertyuioplkjhgfdsazxcvbnm'

#work


@led.on(events.NewMessage(pattern=r'^x', outgoing=True))
async def execute_script(event):
    x = 0
    while True:
        i=0
        while True:
            i += +1
            x += +1
            u3 = str(''.join((random.choice(uss) for i in range(1))))
            u2 = str(''.join((random.choice(uss) for i in range(1))))
            u1 = str(''.join((random.choice(rr) for i in range(1))))
            user = u1 + '_' +u2+ '_' +u3
            print("@"+user)
            if i == 100:
                sleep(2)
                break
            sleep(0.05)
            req = requests.get(f"https://t.me/{user}")
            if req.text.find('Send Message') >= 0:
                if req.text.find(
                        'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
                    pass
                else:
                    try:
                        result = await led(GetFullUserRequest(user))
                        if result:
                            user = result.users[0]
                            last_seen = user.status.was_online
                            if last_seen:
                                print(last_seen.year)
                    except:
                        pass

@led.on(events.NewMessage(pattern=r'^c', outgoing=True))
async def execute_script(event):
    c = os.popen('screen -X -S {} quit')
    print(c)
    if c:
        try: await event.edit(c.read())
        except: await event.edit('True')
    else:
        try:await event.edit(c.errors)
        except:await event.edit("False")

@led.on(events.NewMessage(pattern=r'^d', outgoing=True))
async def execute_script(event):
    
    c = os.popen(f"screen -S mo -dm bash -c 'python3 N1.py; exec sh'")
    print(c)
    if c:
        try: await event.edit(c.read())
        except: await event.edit('True')
    else:
        try:await event.edit(c.errors)
        except:await event.edit("False")

led.run_until_disconnected()
