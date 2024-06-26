from pyrogram import Client


API_ID = 18208497
API_HASH = "b9f8cdba86d3406944419974334e34d5"
BOT_TOKEN = "5170934938:AAHWTgb6FH676fzS-JI3lxxomESplXS8ai0"

Bot = Client(name='Bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN,  plugins={"root": "plugins"})
