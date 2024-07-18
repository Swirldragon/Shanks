import random
from plugins.ping import photos
from database.db import db

import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaDocument

from bot import Bot

setting_b = [
            [InlineKeyboardButton("* Caption *", callback_data = "caption")],
            [InlineKeyboardButton("* Thumbnail *", callback_data = "thumbnail")],
            [InlineKeyboardButton("* Auto Mode *", callback_data = "auto")],
            [InlineKeyboardButton("* Close *", callback_data = "close")],
            ]

mode_S = [
	[InlineKeyboardButton("* Video *", callback_data = "video")],
        [InlineKeyboardButton("* Document *", callback_data = "doc")],
	[InlineKeyboardButton("* Close *", callback_data = "close")],
       ]


async def show_settings(client: Client, message: Message)
    image = random.choice(photos)
    await client.send_photo(chat_id=message.from_user.id, photo=image, caption="List of Setting:", reply_markup=InlineKeyboardMarkup(setting_b))


async def on_set_caption(client: Client, message: Message):
            if len(message.command) == 1:
                        return await message.reply_text("**Give me a caption to set.\n\nExample:- `/setcaption File Name`\n\n For Auto Rename\n\nExample :</b> <code> /setcaption Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @Wizard_Bots </code>**")
            caption = message.text.split(" ", 1)[1]
            await db.set_caption(message.from_user.id, caption=caption)
            await message.reply_text("**Your Caption successfully added ✅**")


async def on_set_mode(client: Client, message: Message):
	mode = await db.get_mode(message.from_user.id)
	await message.reply(f"<b>Your File Mode: {'Video' if mode else 'Document'}</b>", reply_markup=InlineKeyboardMarkup(mode_S))
