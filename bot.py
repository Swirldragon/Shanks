from config import API_HASH, APP_ID, LOGGER, BOT_TOKEN, PORT

from pyrogram import Client

app = Client("my_bot", 
             api_id=API_ID, 
             api_hash=API_HASH, 
             bot_token=BOT_TOKEN)

app.start()

app.stop()
