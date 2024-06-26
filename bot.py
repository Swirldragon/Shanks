from config import API_ID, API_HASH, BOT_TOKEN, LOGGER

from aiohttp import web
import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

Bot = Client('Bot',
             bot_token=BOT_TOKEN,
             plugins={
                "root": "plugins"
            }
            )
