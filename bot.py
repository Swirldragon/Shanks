from config import API_ID, API_HASH, BOT_TOKEN, LOGGER

from aiohttp import web
import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

class Bot:
  def __init__(self):
    super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={
                "root": "plugins"
            },
            bot_token=TG_BOT_TOKEN
    )
    self.LOGGER = LOGGER
    
  async def start(self):
     await super().start()
     
  async def stop(self, *args):
     await super().stop()
