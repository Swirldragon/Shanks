from config import API_ID, API_HASH, BOT_TOKEN

from pyrogram import Client

class bot:
  def __init__(self):
    super().__init__("Bot",
                     api_id=API_ID,
                     api_hash=API_HASH,
                     bot_token=BOT_TOKEN)
    
  async def start(self):
     await super().start()
     
  async def stop(self, *args):
     await super().stop()
