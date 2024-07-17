from cloudscraper import create_scraper
from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# url = "https://insta-dl.hazex.workers.dev/?url=https://instagram.com/reel/ABC"

@Bot.on_message(filters.private & filters.text & filters.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'))
async def instra_reels(client: Client, message: Message):
  await message.reply("Featching The Url")
  urls = message.text
  try:
    
    cget = create_scraper().request
    rjson = cget('GET', f'https://insta-dl.hazex.workers.dev/?url={urls}').json()
    vlink = rjson["url"]
    downloaded = await client.download(vlink)
    await bot.send_video(message.from_user.id, video=downloaded)
    
  except:
    await message.reply_text("Sorry! There Problem at Link. Check Link is Public Or Private.")
  
