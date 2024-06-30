import random
from plugins.start import photos
#from plugins.database.db import *

import asyncio
from pyrogram import types, errors, Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaDocument

from bot import Bot

setting_b = [
            [InlineKeyboardButton("* Rename *", callback_data = "rename")],
            [InlineKeyboardButton("* Request Approval *", callback_data = "ra")],
            [InlineKeyboardButton("* PDf *", callback_data = "pdf")],
            [InlineKeyboardButton("* Converter *", callback_data = "converter")],
            [InlineKeyboardButton("* Close *", callback_data = "close")],
            ]

@Bot.on_message(filters=filters.command(['setting'])) 
async def on_setting(client: Client, message: Message):
    image = random.choice(photos)
    await client.send_photo(chat_id=message.from_user.id, photo=image, caption="List of Setting:", reply_markup=InlineKeyboardMarkup(setting_b))
                     
