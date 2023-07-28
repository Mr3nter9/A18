from time import sleep; import requests
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.sync import TelegramClient , functions , events
import asyncio
import os
id='5229914714'
token='6183317549:AAGB5jAoTSGSc0M0Y_8WR7kEa7oYbyjshM0'
numb_s ='1'
user='dex33bot'
led=TelegramClient('Dex_Tsh', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
led.start()

async def spammer():
 await led.send_message('botfather', '/newbot')
 sleep(0.5)
 await led.send_message('botfather', 'Dex')
 while True:
  i = 0
  while True:
   i += +1
   if i == 100:
    sleep(1.4)
    break
   sleep(0.17)
   req = requests.get(f"https://t.me/{user}")
   if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
    await led.send_message('botfather', user)
    sleep(2)

   else:
    print(f"NOOO : {user}" +' '+ str(i))



async def execute_script(event):
    user = event.message.message[2:]
    x = 0
    while True:
     i = 0
     while True:
      i += +1
      x += +1
      if i == 100:
       sleep(1.4)
       break
      sleep(2)
      req = requests.get(f"https://t.me/{user}")
      if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
       take = await led(UpdateUsernameRequest(user))
       if take :
        requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text=« new hutting »
« UserName » : « @{user} »
---------------------------------
« attempts » : « {x} »
----------------------------------
« Save » : « Channel »
----------------------------------
« owner » :  @isiraqi »""")
      else:
       print(f"NOOO : {user}" + ' ' + str(i)+" "+str(x))


loop = asyncio.get_event_loop()
loop.run_until_complete(spammer())

led.run_until_disconnected()
