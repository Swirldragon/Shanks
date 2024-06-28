from bot import Bot
import random
from pyrogram import Client, filters
import pyrogram.errors
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaDocument

photos = ( "https://graph.org/file/0c85bf7ce08bbb2bdd7b4.jpg",
           "https://graph.org/file/f99c470a76c65a1e1232d.jpg",
           "https://graph.org/file/ffbc541990d0489cbb538.jpg",
           "https://graph.org/file/4ac10607462346840a323.jpg",
           "https://graph.org/file/c3baa04ca9365e4e11dac.jpg",)

START_TEXT = "Hey {}!\n\nI'm A Multi-Function Bot, i can rename files and can do many useful stuff click on Help button to know my secrets."
ACCEPTED_TEXT = "Hey {user}\n\nYour Request For {chat} Is Accepted ✅"
GROUP_TEXT = "<b>Hey {}!\n\nShanks here, use [/help](https://t.me/ShanksXRobot?start=help) to know my cmds.</b>"

button = [[        
        InlineKeyboardButton('* Help *', url= "https://t.me/ShanksXRobot?start=help"),
        InlineKeyboardButton("* Settings *", callback_data = "setting")
    ]]
keyboard = InlineKeyboardMarkup([[button]])

@Bot.on_message(filters=filters.command(['start'])) 
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


@Bot.on_message(filters=filters.command(['start']) & filters.group) 
async def start_process(client: Client, message: Message):
           image = random.choice(photos)
           await message.reply_photo(photo=image, caption=GROUP_TEXT.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(button), reply_to_message_id=message.from_user.id)


@Bot.on_callback_query()
async def cb_help(client: Bot, query: CallbackQuery):
           data = query.data
           if data == "help":
