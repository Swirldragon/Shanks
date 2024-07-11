from bot import Bot
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.db import db

setting_b = [
            [InlineKeyboardButton("* Caption *", callback_data = "caption")],
            [InlineKeyboardButton("* Thumbnail *", callback_data = "thumbnail")],
            [InlineKeyboardButton("* Auto Mode *", callback_data = "auto")]
            [InlineKeyboardButton("* Close *", callback_data = "close")],
            ]

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
      user_id = query.from_user.id
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
                  text = "<b>☆ Rename Function:\n\nWe Currently Have Three Modes In Our Bot..\n\n•Auto Mode : This Will Rename Your Files Auto. To Setup This Function Use <code>/setting</code>.\n\n• Manual: This Is Doned By <code>/rename Ch-123 @Manga_Arena.pdf</code>\n\nMade By @Wizard_Bots.</b>",
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
                              [InlineKeyboardButton(" Close", callback_data = "close")],
                        ]
                  )
            )
      elif data == "caption":
            caption = await db.get_caption(user_id)
            if caption:
                   await query.message.edit_text(
                         text = f"Your Caption : {caption}",
                         disable_web_page_preview = True,
                         reply_markup = InlineKeyboardMarkup(
                               [
                                     [InlineKeyboardButton("* Back *", callback_data = "s_back")],
                                     [InlineKeyboardButton("* Close *", callback_data = "close")],
                                     [InlineKeyboardButton("* Delete *", callback_data = "c_delete")],
                               ]
                         ))
            else:
                  await query.answer("YOU HAVE NOT SET CAPTION .", show_alert=True)
 
      elif data == "c_delete":
            await db.set_caption(user_id, caption=None)
            await query.answer("YOUR CAPTION DELETED.", show_alert=True)
            
      elif data == "s_back":
            await query.message.edit_text(
                  text = "List of Setting:",
                  disable_web_page_preview = True,
                  reply_markup = InlineKeyboardMarkup(setting_b)
            )
            
      elif data == "thumbnail":
            thumb = await db.get_thumbnail(user_id)
            if thumb:
                  await query.message.edit_text(
                        text = "Your Thumbnail:",
                        disable_web_page_preview = True,
                        reply_markup = InlineKeyboardMarkup(
                              [
                                    InlineKeyboardButton("* View *", callback_data = "t_view"),
                                    InlineKeyboardButton("* Delete *", callback_data = "t_delete")
                              ]
                        ))
            else:
                  await query.answer("YOU HAVENOT SET THUMBNAIL.", show_alert=True)
                  
      elif data == "t_view":
            thumb = await db.get_thumbnail(user_id)
            await client.send_photo(chat_id=user_id, photo=thumb)
            
      elif data == "t_delete":
            await db.get_thumbnail(user_id, caption=None)
            await query.answer("YOUR THUMBNALI DELETED.", show_alert=True)
            
      elif data == "close":
            await query.message.delete()
            try:
                  await query.message.reply_to_message.delete()  
            except:
                  pass
