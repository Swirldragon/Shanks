from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

AUTO-TEXT = """ ☆ Auto-ReqAccept:

↳ Add Me In Your Channel To Use
↳ I Auto Accept The Users To Channel

↳ Made By @Wizard_Bots """

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "Help":
        await query.message.edit_text(
            text = "List of modules:",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                      InlineKeyboardButton("🔒 Auto-ReqAccept", callback_data = "autoreqaccept"),
                      InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "autoreqaccept":
      await query.message.edit_text(
            text = AUTO-TEXT,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Back", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
