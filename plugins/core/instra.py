from cloudscraper import create_scraper
from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from .utils import progress_for_pyrogram, humanbytes, convert
import json
import time
import asyncio

# url = "https://insta-dl.hazex.workers.dev/?url=https://instagram.com/reel/ABC"


async def instra_reels(client, message):
  if "https://www.instagram.com/" in message.text:
    user_id = message.from_user.id
    urls = message.text
    msg = await message.reply("<code>Featching The Url....</code>")
    cget = create_scraper().request
    rjson = cget('GET', f'https://insta-dl.hazex.workers.dev/?url={urls}').json()
    try:
      vlinks = rjson["result"]
      vlink = vlinks["url"]
      caption = "<b>Doned By @ShanksXRobot</b>"
      await client.send_video(user_id, vlink, caption=caption)
      await msg.delete()
    except Exception as e:
      exmsg = await message.reply_text("<b>Check Your Link is Private or Story.</b>")
      await client.send_message(-1001885135958, f"Instra Errors - <code>{e}</code>")
      await msg.delete()
      await asyncio.sleep(6)
