from .core.autorename import auto_rename_files
from .core.convertor import convert_pdf_to_cbz, convert_cbz_to_pdf
from .core.decryptPDF import decrypt_pdf
from .core.encryptPDF import encrypt_pdf
from .core.instra import instra_reels
from .core.rename import rename_files
from .ping import start_command
from .settings import show_settings, on_set_caption, mode

from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot

@Bot.on_message(filters=filters.command(["start"]))
async def handle_start(client: Client, message: Message):
  await start_command(client, message)

@Bot.on_message(filters=filters.command(["setting"]))
async def handle_setting(client: Client, message: Message):
  await on_set_caption(client, message)

@Bot.on_message(filters=filters.command(["sethumb"]))
async def on_set_thumb(client: Client, message: Message):
	await message.reply("Send Me Your Thumbnali")

@Bot.on_message(filters=filters.command(["setcaption"]))
async def handle_captain(client: Client, message: Message):
  await on_set_caption(client, message)

@Bot.on_message(filters.private & filters.photo)
async def addthumbs(client: Client, message: Message):
	await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)
	await message.reply("You have set thumb")

@Bot.on_message(filters=filters.command(["mode"]))
async def handle_mode(client: Client, message: Message):
  await on_set_mode(client, message)
  
@Bot.on_message(filters=filters.command(["encryptPDF"]))
async def handle_encrypt_pdf(client: Client, message: Message):
  await encrypt_pdf(client, message)


@Bot.on_message(filters=filters.command(["rename"]))
async def handle_rename(bot: Bot, msg: Message):
  await rename_files(bot, msg)

@Bot.on_message(filters.text & filters.private)
async def handle_instra_reels(client: Client, message: Message):
  await instra_reels(client, message)

@Bot.on_message(filters=filters.command(["decryptpdf"]))
async def handle_decryptpdf(client: Client, message: Message):
  await decrypt_pdf(client, message)

@Bot.on_message(filters=filters.command(["p2c"]))
async def handle_decryptpdf(client: Client, message: Message):
  await convert_pdf_to_cbz(client, message)

@Bot.on_message(filters=filters.command(["c2p"]))
async def handle_decryptpdf(client: Client, message: Message):
  await convert_cbz_to_pdf(client, message)

""" @Bot.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def auto_rename_files(client: Client, message: Message):
  await auto_rename_files(client, message)"""
