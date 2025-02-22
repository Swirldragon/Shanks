from bot import Bot
import random
from pyrogram import Client, filters
import pyrogram.errors
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaDocument
from database.add import add_user_to_database

photos = ( "https://graph.org/file/ffbc541990d0489cbb538.jpg",
           "https://graph.org/file/4ac10607462346840a323.jpg",
           "https://graph.org/file/0c85bf7ce08bbb2bdd7b4.jpg",)

START_TEXT = "<b>Hey {}!\n\nI'm A Multi-Function Bot, i can rename files and can do many useful stuff click on Help button to know my secrets.</b>"
ACCEPTED_TEXT = "<b>Hey {user}\n\nYour Request For {chat} Is Accepted ✅</b>"
GROUP_TEXT = "<b>Hey {}!\n\nShanks here, use [/start](https://t.me/ShanksXRobot?start=start) to know my cmds.</b>"

button = [[        
        InlineKeyboardButton('* Help *', callback_data = "help"),
        InlineKeyboardButton("* Settings *", url = "https://t.me/ShanksXRobot?start=setting")
    ]]

gbutton = [[        
        InlineKeyboardButton('* Start Now *', url = "https://t.me/ShanksXRobot?start=start"),
        InlineKeyboardButton("* Channel *", url = "https://t.me/Wizard_Bots")
    ]]



async def start_command(client, message):
           user_id = message.from_user.id
           if len(message.command) > 1:
                      if verify_token_memory(user_id, token):
                                 await message.reply("Token verified! You can now use the bot.")
                                 save_token(user_id, token, dr)
                                 global_tokens.pop(user_id, None)
           image = random.choice(photos)
           user_id = message.from_user.id
           if not user_id:
                      return await message.reply_text("I don't know about you sir :(")
           await add_user_to_database(client, message)
           await client.send_photo(chat_id=message.from_user.id, photo=image, caption=START_TEXT.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(button))
        
#Auto-ReqAccept Function

@Bot.on_chat_join_request()
async def req_accept(client: Client, message: Message):
           user_id = message.from_user.id
           chat_id = message.chat.id
           await client.approve_chat_join_request(chat_id, user_id)
           try: await client.send_message(user_id, ACCEPTED_TEXT.format(user=message.from_user.mention, chat=message.chat.title))
           except Exception as e: await client.send_message(-1001885135958, f"{e}")



async def start_process(client: Client, message: Message):
           image = random.choice(photos)
           await client.send_photo(chat_id=message.chat.id, photo=image, caption=GROUP_TEXT.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(gbutton))
