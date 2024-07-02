from pyrogram import Client
from aiohttp import web
from plugins import web_server

API_ID = 18208497
API_HASH = "b9f8cdba86d3406944419974334e34d5"
BOT_TOKEN = "5170934938:AAHWTgb6FH676fzS-JI3lxxomESplXS8ai0"
LOG_CHANNEL = -1001885135958
DB_URL = "mongodb+srv://shankswillson33:shankswillson33@cluster0.vshfo6u.mongodb.net/?retryWrites=true&w=majority"

Bot = Client(name='Bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN,  plugins={"root": "plugins"})

class Bot(Client):
    def __init__(self):
      super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            }
        )
      
    async def start(self):
      await super().start()
      usr_bot_me = await self.get_me()
      self.uptime = datetime.now()
      #web-response
      app = web.AppRunner(await web_server())
      await app.setup()
      bind_address = "0.0.0.0"
      await web.TCPSite(app, bind_address, PORT).start()
      
    async def stop(self, *args):
      await super().stop()
      self.LOGGER(__name__).info("Bot stopped.")
