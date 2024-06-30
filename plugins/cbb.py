from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

AUTO_TEXT = "☆ Auto-ReqAccept:\n\n↳ Add Me In Your Channel To Use\n↳ I Auto Accept The Users To Channel\n\n↳ Made By @Wizard_Bots."

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "rename":
        await query.message.edit_text(
            text = "Your Rename Settings:",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                        [InlineKeyboardButton("UPLOAD AS DOCUMENT", callback_data = "upload_as_doc")],
                        [InlineKeyboardButton("APPLY CAPTION", callback_data = "ApplyDefaultCaption")],
                        [InlineKeyboardButton("𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽", callback_data = "setCustomCaption")],
                        [InlineKeyboardButton("𝚂𝙴𝚃 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻", callback_data = "setThumbnail")],
                        [InlineKeyboardButton("MEGA EMAIL", callback_data = "megaemail")],
                        [InlineKeyboardButton("MEGA PASSWORD", callback_data = "megapass")],
                        [InlineKeyboardButton("Auto Rename", callback_data = "auto_rename")],
                        [InlineKeyboardButton("Close", callback_data = "close")],
                ]
            )
        )
  
