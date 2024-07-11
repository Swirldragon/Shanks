import random
from plugins.start import photos
from database.db import db

import asyncio
from pyrogram import types, errors, Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaDocument

from bot import Bot

setting_b = [
            [InlineKeyboardButton("* Caption *", callback_data = "caption")],
            [InlineKeyboardButton("* Thumbnail *", callback_data = "thumbnail")],
            [InlineKeyboardButton("* Auto Mode *", callback_data = "auto")],
            [InlineKeyboardButton("* Close *", callback_data = "close")],
            ]

@Bot.on_message(filters=filters.command(['setting'])) 
async def show_settings(client: Client, message: Message):
    image = random.choice(photos)
    await client.send_photo(chat_id=message.from_user.id, photo=image, caption="List of Setting:", reply_markup=InlineKeyboardMarkup(setting_b))

@Bot.on_message(filters=filters.command(['setcaption']))
async def on_set_caption(client: Client, message: Message):
            if len(message.command) == 1:
                        return await message.reply_text("**Give me a caption to set.\n\nExample:- `/setcaption File Name`\n\n For Auto Rename\n\nExample :</b> <code> /setcaption Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @Wizard_Bots </code>**")
            caption = message.text.split(" ", 1)[1]
            await db.set_caption(message.from_user.id, caption=caption)
            await message.reply_text("**Your Caption successfully added ✅**")
	
@Bot.on_message(filters=filters.command(['setthumb']))
async def on_set_thumb(client: Client, message: Message):
	message.reply("Send Me Your Thumbnali")
	
@Bot.on_message(filters.private & filters.photo)
async def addthumbs(client: Client, message: Message):
	await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)
	awaitmessage.reply("You have set thumb")
