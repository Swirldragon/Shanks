import time, os
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from .utils import progress_for_pyrogram, humanbytes
from bot import Bot 
from database.db import db


@Bot.on_message(filters=filters.command(["rename"]))
async def rename_files(bot: Bot, msg: Message):
  user_id = msg.from_user.id
  reply = msg.reply_to_message
  CAPTION = await db.get_caption(user_id)
  if len(msg.command) < 2 or not reply:
    return await msg.reply_text("Please Reply To An File or video or audio With filename + .extension eg:-(`.mkv` or `.mp4` or `.zip`)")   
  media = reply.document or reply.audio or reply.video
  if not media:
    await msg.reply_text("Please Reply To An File or video or audio With filename + .extension eg:-(`.mkv` or `.mp4` or `.zip`)")
  og_media = getattr(reply, reply.media.value)
  new_name = msg.text.split(" ", 1)[1]
  sts = await msg.reply_text("Trying to Downloading.....")
  c_time = time.time()
  downloaded = await reply.download(file_name=new_name, progress=progress_for_pyrogram, progress_args=("Download Started.....", sts, c_time)) 
  filesize = humanbytes(og_media.file_size)                
  if CAPTION:
    try:
      cap = CAPTION.format(file_name=new_name, file_size=filesize)
    except Exception as e:
      pass                            
  else:
    cap = f"{new_name}\n\n💽 size : {filesize}"
    # this idea's back end is MKN brain 🧠
  
  DOWNLOAD_LOCATION = f"downloads/{new_name}"

  dir = os.listdir(DOWNLOAD_LOCATION)
  if len(dir) == 0:
    file_thumb = await bot.download_media(og_media.thumbs[0].file_id) 
    og_thumbnail = file_thumb
  else:
    try:
      og_thumbnail = f"{user_id}/thumbnail.jpg"
    except Exception as e:
      print(e)          
      og_thumbnail = None
        
  await sts.edit("Trying to Uploading")
  c_time = time.time()
  try:
    await bot.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_for_pyrogram, progress_args=("Uploade Started.....", sts, c_time))        
  except Exception as e:  
    return await sts.edit(f"Error {e}")                       
  try:
    if file_thumb:
      os.remove(file_thumb)
    os.remove(downloaded)      
  except:
    pass
  await sts.delete()
