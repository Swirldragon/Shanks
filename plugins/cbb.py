from pyrogram import __version__
from bot import Bot
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.db import db
from .settings import show_settings

      
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
      usr_id = query.from_user.id
      user_data = await db.get_user_data(usr_id)
      if not user_data:
            await message.edit("Failed to fetch your data from database!")
            return
      upload_as_doc = user_data.get("upload_as_doc", False)
      caption = user_data.get("caption", None)
      apply_caption = user_data.get("apply_caption", False)
      thumbnail = user_data.get("thumbnail", None)
      megaemail = user_data.get("megaemail", None)
      megapassword = user_data.get("megapassword", None)
      auto = user_data.get("auto", None)
      data = query.data
      if data == "help":
            await query.message.edit_text(
                  text = "<b>List of modules:</b>",
                  disable_web_page_preview = True,
                  reply_markup = InlineKeyboardMarkup(
                        [
                              [InlineKeyboardButton("* Rename *", callback_data = "ab_rename")],
                              [InlineKeyboardButton("* Request Approval *", callback_data = "ra")],
                              [InlineKeyboardButton("* PDf *", callback_data = "pdf")],
                              [InlineKeyboardButton("* Converter *", callback_data = "converter")],
                              [InlineKeyboardButton("Close", callback_data = "close")],
                        ]
                  )
            )

      elif data == "ab_rename":
            await query.message.edit_text(
                  text = "<b>☆ Rename Function:\n\nWe Currently Have Three Modes In Our Bot..\n\n•Auto Mode : This Will Rename Your Files Auto With using <code>/rename</code> Function.\n\n• Manual: This Is Doned By <code>/rename Ch-123 @Manga_Arena.pdf</code>.\n\n•Mega: This Rename The Files At Mega Account Folders. It Can Rename Whole Files In Folder at Time. Use <code>/mega</code>.\n\n To Set Caption, Thumbnail, Mega Email and Password Use <code>/setting</code>\n\nMade By @Wizard_Bots.</b>",
                  disable_web_page_preview = True,
                  reply_markup = InlineKeyboardMarkup(
                        [
                              [
                                    InlineKeyboardButton("CLOSE", callback_data = "close"),
                                    InlineKeyboardButton("BACK", callback_data = "back")
                              ]
                        ]
                  )
            )

      elif data == "ra":
            await query.message.edit_text(
                  text = "<b>☆ Auto-ReqAccept:\n\n Add Me In Your Channel To Use\n I Auto Accept The Users To Channel\n\n Made By @Wizard_Bots.</b>",
                  disable_web_page_preview = True,
                  reply_markup = InlineKeyboardMarkup(
                        [
                              [
                                    InlineKeyboardButton("CLOSE", callback_data = "close"),
                                    InlineKeyboardButton("BACK", callback_data = "back")
                              ]
                        ]
                  )
            )
            
      elif data == "rename": 
            await query.message.edit_text(
                  text = "<b>Your Rename Settings:</b>",
                  disable_web_page_preview = True,
                  reply_markup = InlineKeyboardMarkup(
                        [
                              [InlineKeyboardButton(f"UPLOAD AS DOCUMENT {'✅' if upload_as_doc else '🗑️'}", callback_data = "upload_as_doc")],
                              [InlineKeyboardButton(f"APPLY CAPTION {'✅' if apply_caption else '🗑️'}", callback_data = "triggerApplyCaption")],
                              [InlineKeyboardButton(f"SET CAPTION {'🗑️' if caption else '✅'}", callback_data = "setCustomCaption")],
                              [InlineKeyboardButton(f"{'CHANGE' if thumbnail else 'SET'} THUMBNAIL", callback_data = "Thumbnail")],
                              [InlineKeyboardButton(f"MEGA EMAIL {'✅' if megaemail else '🗑️'}", callback_data = "megaemail")],
                              [InlineKeyboardButton(f"MEGA PASSWORD {'✅' if megapassword else '🗑️'}", callback_data = "megapass")],
                              [InlineKeyboardButton(f"AUTO RENAME {'✅' if auto else '🗑️'}", callback_data = "auto_rename")],
                              [InlineKeyboardButton("CLOSE", callback_data = "close")],
                        ]
                  )
            )

      elif data == "upload_as_doc":
            pass
      elif data == "setCustomCaption":
            await query.answer()
            #making it 
      elif data == "triggerApplyCaption":
            await query.answer()
            apply_caption = await db.get_apply_caption(query.from_user.id)
            if not apply_caption:
                  await db.set_apply_caption(query.from_user.id, True)
            else:
                  await db.set_apply_caption(query.from_user.id, False)
            await show_settings(query.message)
            
      elif data == "Thumbnail":
            thumbnail = await db.get_thumbnail(query.from_user.id)
            if not thumbnail:
                  await query.answer(text="YOU DIDN'T SET ANY CUSTOM THUMBNAIL!", show_alert=True)
            else:
                  await query.answer()
                  await message.send_photo(query.message.chat.id, thumbnail, "CUSTOM THUMBNAIL",
                                          reply_markup=types.InlineKeyboardMarkup(
                                                [
                                                      [InlineKeyboardButton("DELETE THUMBNAIL", callback_data="deleteThumbnail")]
                                                ]
                                          )
                                         )
      elif data == "deleteThumbnail":
            await db.set_thumbnail(query.from_user.id, None)
            await query.answer("OKAY, I DELETED YOUR CUSTOM THUMBNAIL. NOW I WILL APPLY DEFAULT THUMBNAIL.", show_alert=True)
            await query.message.delete(True)

      elif data == "setThumbnail":
            await query.answer()
            await query.message.edit("SEND ME ANY PHOTO TO SET THAT AS CUSTOM THUMBNAIL.\n\nPRESS <code>/cancel</code> TO CANCEL PROCESS..")        
            from_user_thumb: "message" = await client.listen(query.message.chat.id)
            if not from_user_thumb.photo:
                  await message.edit("<b>PROCESS CANCELLED</b>")
                  return await from_user_thumb.continue_propagation()
            else:
                  await db.set_thumbnail(query.from_user.id, from_user_thumb.photo.file_id)
                  await query.message.edit("OKAY\nNOW I WILL APPLY THIS THUMBNAIL TO NEXT UPLOADS.",
                                            reply_markup=types.InlineKeyboardMarkup(
                                                  [[InlineKeyboardButton("RENAME SETTING",
                                                                   callback_data="rename")]]
                                            ))
      elif data == "megaemail":
            pass
      elif data == "megapass":
            pass
      elif data == "auto_rename":
            pass
      elif data == "back":
            await query.message.edit_text(
                  text = "<b>List of modules:</b>",
                  disable_web_page_preview = True,
                  reply_markup = InlineKeyboardMarkup(
                        [
                              [InlineKeyboardButton("* Rename *", callback_data = "ab_rename")],
                              [InlineKeyboardButton("* Request Approval *", callback_data = "ra")],
                              [InlineKeyboardButton("* PDf *", callback_data = "pdf")],
                              [InlineKeyboardButton("* Converter *", callback_data = "converter")],
                              [InlineKeyboardButton("Close", callback_data = "close")],
                        ]
                  )
            )
            
      elif data == "close":
            await query.message.delete()
            try:
                  await query.message.reply_to_message.delete()  
            except:
                  pass
