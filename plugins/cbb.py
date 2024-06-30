from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

      
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
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
                            [InlineKeyboardButton("UPLOAD AS DOCUMENT", callback_data = "upload_as_doc")],
                            [InlineKeyboardButton("CAPTION", callback_data = "setCustomCaption")],
                            [InlineKeyboardButton("THUMBNAIL", callback_data = "setThumbnail")],
                            [InlineKeyboardButton("MEGA EMAIL", callback_data = "megaemail")],
                            [InlineKeyboardButton("MEGA PASSWORD", callback_data = "megapass")],
                            [InlineKeyboardButton("AUTO RENAME", callback_data = "auto_rename")],
                            [InlineKeyboardButton("CLOSE", callback_data = "close")],
                      ]
                )
          )
     
    elif data == "upload_as_doc":
          pass
    elif data == "setCustomCaption":
          pass
    elif data == "setThumbnail":
          pass
    elif data == "megaemail":
          pass
    elif data == "megapass":
          pass
    elif data == "auto_rename":
          pass
    elif data == "help":
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
  
