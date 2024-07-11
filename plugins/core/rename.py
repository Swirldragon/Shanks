import time, os
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from .utils import progress_for_pyrogram, humanbytes, convert
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
  
  c_thumb = await db.get_thumbnail(user_id)
  if c_thumb:
    ph_path = await client.download_media(c_thumb)
    print(f"Thumbnail downloaded successfully. Path: {ph_path}")
  elif not type or msg.video.thumbs:
    ph_path = await bot.download_media(msg.video.thumbs[0].file_id)
    
  if ph_path:
    Image.open(ph_path).convert("RGB").save(ph_path)
    img = Image.open(ph_path)
    img.resize((320, 320))
    img.save(ph_path, "JPEG")  

        
  await sts.edit("Trying to Uploading")
  c_time = time.time()
  try:
    await bot.send_document(msg.chat.id, document=downloaded, thumb=ph_path, caption=cap, progress=progress_for_pyrogram, progress_args=("Uploade Started.....", sts, c_time))        
  except Exception as e:  
    return await sts.edit(f"Error {e}")                       
  try:
    if ph_path:
      os.remove(ph_path)
    os.remove(downloaded)      
  except:
    pass
  await sts.delete()
