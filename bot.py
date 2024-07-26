from pyrogram import Client
from aiohttp import web
from plugins import web_server
import pyromod.listen
import os

API_ID = 18208497
API_HASH = "b9f8cdba86d3406944419974334e34d5"
BOT_TOKEN = "5170934938:AAHWTgb6FH676fzS-JI3lxxomESplXS8ai0"
LOG_CHANNEL = -1001885135958
DB_URL = "mongodb+srv://justatestsubject01:HzP5SK8ZiiLHcF3o@cluster0.wizfkbo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
PORT = 8080
ADMINS = 1880221341

Bot = Client(name='Bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN,  plugins={"root": "plugins"})

""" class Bot(Client):

  def __init__(self):
    super().__init__(
      "Shanks",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN,
      plugins={
        "root": "plugins"
      }
    )
    
  async def start(self):

    await super().start()
    print('Bot Is Start')
    #web-response
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    print("web Stites Pass")

  async def stop(self, *args):

    await super().stop()
    print('Bot Stop') """
