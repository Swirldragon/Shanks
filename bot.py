from config import API_HASH, API_ID, LOGGER, BOT_TOKEN, PORT

from pyrogram import Client

class Bot(Client):
    def __init__(self):
        super().__init__("my_bot",
                         api_id=API_ID,
                         api_hash=API_HASH, 
                         bot_token=BOT_TOKEN)
        bot.start()
        bot.stop()
