import random
from plugins.start import photos
#from plugins.database.db import *

import asyncio
from pyrogram import types, errors, Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaDocument

from bot import Bot

setting_b = [
            [InlineKeyboardButton("* Rename *", callback_data = "rename")],
            [InlineKeyboardButton("* Request Approval *", callback_data = "f2l")],
            [InlineKeyboardButton("* PDf *", callback_data = "pdf")],
            [InlineKeyboardButton("* Converter *", callback_data = "converter")],
            ]

@Bot.on_message(filters=filters.command(['setting'])) 
async def on_setting(client: Client, message: Message):
    image = random.choice(photos)
    await client.send_photo(chat_id=message.from_user.id, photo=image, caption="List of Setting:", reply_markup=InlineKeyboardMarkup(setting_b))

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "rename":
        await query.message.edit_text(
            text = "Your Rename Settings:",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                        [InlineKeyboardButton("UPLOAD AS DOCUMENT", callback_data = "upload_as_doc")],
                        [InlineKeyboardButton("APPLY CAPTION", callback_data = "ApplyDefaultCaption")],
                        [InlineKeyboardButton("𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽", callback_data = "setCustomCaption")],
                        [InlineKeyboardButton("𝚂𝙴𝚃 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻", callback_data = "setThumbnail")],
                        [InlineKeyboardButton("MEGA EMAIL", callback_data = "megaemail")],
                        [InlineKeyboardButton("MEGA PASSWORD", callback_data = "megapass")],
                ]
            )
        )
        
                        
