from pyrogram import __version__
from bot import Bot
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.db import db
from .settings import show_settings

handler_dict = {}

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
      usr_id = query.from_user.id
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
