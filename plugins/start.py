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

START_TEXT = "Hey {}!\n\nI'm A Multi-Function Bot, i can rename files and can do many useful stuff click on Help button to know my secrets."
ACCEPTED_TEXT = "Hey {user}\n\nYour Request For {chat} Is Accepted ✅"

button = [[        
        InlineKeyboardButton('😊 Help', callback_data = "help"),
        InlineKeyboardButton("🔒 Settings", callback_data = "setting")
    ]]
keyboard = InlineKeyboardMarkup([[button]])

@Bot.on_message(filters.command("start") & filters.private) 
async def start_command(client: Client, message: Message):
    image = random.choice(photos)
    user = await client.get_users(message.from_user.id)
    username = user.username
    name = user.first_name
    chat_id = message.from_user.id
    await message.reply_photo(photo=image, caption=START_TEXT.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(button), reply_to_message_id=message.from_user.id)

#Auto-ReqAccept Function

@Bot.on_chat_join_request()
async def req_accept(client: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await client.approve_chat_join_request(chat_id, user_id)
    try: await client.send_message(user_id, ACCEPTED_TEXT.format(user=message.from_user.mention, chat=message.chat.title))
    except Exception as e: print(e)
