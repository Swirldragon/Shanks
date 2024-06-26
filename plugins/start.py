from bot import Bot
import random
from pyrogram import Client, filters
import pyrogram.errors
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaDocument

photos = ( "https://graph.org/file/e93290b99f1a87211ee7c.jpg",
           "https://graph.org/file/ccf9d8a22e8220990850d.jpg",
           "https://graph.org/file/5e9f4d6b735a19e973d12.jpg",
           "https://graph.org/file/8cc2e4d1ccf20ecec6d8b.jpg",
           "https://graph.org/file/342f8b723a35dfbb2d2b5.jpg",
           "https://graph.org/file/ef3c23fa7f07d2078e2c9.jpg",
           "https://graph.org/file/e358de4b9807c4c5a1cd6.jpg",
           "https://graph.org/file/4523cccaf531c8fcbdc79.jpg",)


@Bot.on_message(filters.command("start") & filters.private) 
async def start_command(client: Client, message: Message):
    image = random.choice(photos)
    user = await client.get_users(message.from_user.id)
    username = user.username
    name = user.first_name
    await message.reply(photo=image, caption=f"Hey [{name}](https://t.me/{username})\n\nI'm A Multi-Function Bot, i can rename files and can do many useful stuff click on Help button to know my secrets",
                        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😊 About Me", callback_data = "about"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
                        )                  
