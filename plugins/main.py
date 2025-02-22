from .core.autorename import auto_rename_files
from .core.convertor import convert_cbz_to_pdf
from .core.decryptPDF import decrypt_pdf
from .core.encryptPDF import encrypt_pdf
from .core.instra import instra_reels
from .core.rename import rename_files
from .ping import start_command, start_process
from .settings import show_settings, on_set_caption, on_set_mode
from .rsc_save import save
from .rsc_generate import login

from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot
from database.db import db, database
from my_token import *

@Bot.on_message(filters=filters.command(["token"]))
async def handle_token(client: Client, message: Message):
	user_id = message.from_user.id
	token = message.command[1]
	await get_token(message, user_id)

@Bot.on_message(filters=filters.command(["c2p"]))
async def handle_c2p(bot: Bot, message: Message):
  await convert_cbz_to_pdf(bot, message)

@Bot.on_message(filters=filters.command(['start']) & filters.group) 
async def handle_startz(client: Client, message: Message):
	await start_process(client, message)
	
@Bot.on_message(filters=filters.command(["start"]))
async def handle_start(client: Client, message: Message):
  await start_command(client, message)

@Bot.on_message(filters=filters.command(["setting"]))
async def handle_setting(client: Client, message: Message):
  await show_settings(client, message)

@Bot.on_message(filters=filters.command(["sethumb"]))
async def on_set_thumb(client: Client, message: Message):
	await message.reply("Send Me Your Thumbnali")

@Bot.on_message(filters=filters.command(["setcaption"]))
async def handle_captain(client: Client, message: Message):
  await on_set_caption(client, message)

@Bot.on_message(filters.private & filters.photo)
async def addthumbs(client: Client, message: Message):
	await db.set_thumbnail(message.from_user.id, thumbnail=message.photo.file_id)
	await message.reply("You have set thumb")

@Bot.on_message(filters=filters.command(["mode"]))
async def handle_mode(client: Client, message: Message):
  await on_set_mode(client, message)
  
@Bot.on_message(filters=filters.command(["encryptPDF"]))
async def handle_encrypt_pdf(client: Client, message: Message):
  await encrypt_pdf(client, message)

@Bot.on_message(filters=filters.command(["login"]))
async def handle_login(bot: Client, message: Message):
	await login(bot, message)

@Bot.on_message(filters=filters.command(["rename"]))
async def handle_rename(bot: Bot, msg: Message):
  await rename_files(bot, msg)

@Bot.on_message(filters.text & filters.private)
async def handle_text(client: Client, message: Message):
	user_id = message.from_user.id
	user_data = verify_token(user_id)
	if "https://t.me/" in message.text:
		if user_id == 1880221341:
			await save(client, message)
		elif user_data == True:
			await save(client, message)
		else:
			await message.reply("<b> Get Your Token By <code>/token</code>.<b/>")
	else:
		await instra_reels(client, message)
  
@Bot.on_message(filters=filters.command(["decryptpdf"]))
async def handle_decryptpdf(client: Client, message: Message):
  await decrypt_pdf(client, message)

@Bot.on_message(filters=filters.command(["c2p"]))
async def handle_cbz_to_pdf(bot: Bot, message: Message):
  await convert_cbz_to_pdf(bot, message)

@Bot.on_message(filters=filters.command(["logout"]))
async def logout(_, msg):
    user_data = database.find_one({"chat_id": msg.chat.id})
    if user_data is None or not user_data.get('session'):
        return 
    data = {
        'session': None,
        'logged_in': False
    }
    database.update_one({'_id': user_data['_id']}, {'$set': data})
    await msg.reply("**Logout Successfully** ♦")
	
""" @Bot.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def auto_rename_files(client: Client, message: Message):
  await auto_rename_files(client, message)"""
