from cloudscraper import create_scraper
from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from .utils import progress_for_pyrogram, humanbytes, convert
import json

# url = "https://insta-dl.hazex.workers.dev/?url=https://instagram.com/reel/ABC"

@Bot.on_message(filters.text & filters.private)
async def instra_reels(client: Client, message: Message):
  if "https://www.instagram.com/" in message.text:
    user_id = message.from_user.id
    msg = await message.reply("Featching The Url")
    urls = message.text
    cget = create_scraper().request
    rjson = cget('GET', f'https://insta-dl.hazex.workers.dev/?url={urls}').json()
    vlinks = rjson["result"]
    vlink = vlinks["url"]
    sts = await msg.reply_text("Trying to Downloading.....")
    c_time = time.time()
    cap = "Made By @Wizard_bots"
    downloaded = await reply.download(file_name=cap, progress=progress_for_pyrogram, progress_args=("Download Started.....", sts, c_time))
    await sts.edit("Trying to Uploading")
    c_time = time.time()
    await bot.send_video(user_id, video=downloaded, caption=cap, progress=progress_for_pyrogram, progress_args=("Uploade Started.....", sts, c_time))
    msg.delete()
    
