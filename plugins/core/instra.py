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
    xxx = []
    try:
      vlinks = rjson["result"]
      vlink = vlinks["url"]
      caption = "<b>Doned By @ShanksXRobot</b>"
      xx = await client.send_video(user_id, vlink, caption=caption)
      await msg.delete()
      xxx.append(xx)
    except Exception as e:
      xx = await message.reply_text("<b>Check Your Link is Private or Story.</b>")
      xxx.append(xx)
      await client.send_message(-1001885135958, f"Instra Errors - <code>{e}</code>")
      await msg.delete()
    await client.delete_messages(message.chat.id,[smsg.id])
    await message.reply_text("<code>Files will be deleted After 10 seconds, Save them to the Saved Message now !!</code>")
    await asyncio.sleep(600)
    
    for xx in xxx:
      try:
        xx.delete()
      except:
        pass
