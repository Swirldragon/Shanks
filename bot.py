from config import env_vars
from aiohttp import web
import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

Bot = Client('Bot',
             api_id=18208497,
             api_hash=b9f8cdba86d3406944419974334e34d5,
             bot_token=5170934938:AAHWTgb6FH676fzS-JI3lxxomESplXS8ai0,
             plugins={
                "root": "plugins"
            }
            )

