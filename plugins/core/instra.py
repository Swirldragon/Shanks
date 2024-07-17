from cloudscraper import create_scraper
from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import json

# url = "https://insta-dl.hazex.workers.dev/?url=https://instagram.com/reel/ABC"

@Bot.on_message(filters.text & filters.private)
async def instra_reels(client: Client, message: Message):
  if "https://www.instagram.com/" in message.text:
    msg = await message.reply("Featching The Url")
    urls = message.text
    cget = create_scraper().request
    rjson = cget('GET', f'https://insta-dl.hazex.workers.dev/?url={urls}').json()
    vlink = rjson["url"]
    downloaded = await client.download(vlink)
    msg.delete()
    await bot.send_video(message.from_user.id, video=downloaded)
    
