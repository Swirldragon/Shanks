from random import choice
from plugins.start import photos
from plugins.database.db import db

import asyncio
from pyrogram import types, errors, Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaDocument

from bot import Bot

setting_b = [
            [InlineKeyboardButton("* Rename *", callback_data = "rename"),
            InlineKeyboardButton("* Request Approval *", callback_data = "f2l")]
            [InlineKeyboardButton("* PDf *", callback_data = "pdf"),
            InlineKeyboardButton("* Converter *", callback_data = "converter")]
            ]

@Bot.on_message(filters=filters.command(['setting'])) 
async def on_setting(client: Client, message: Message):
    image = random.choice(photos)
    await client.send_photo(chat_id=message.from_user.id, photo=image, caption="List of Setting:", reply_markup=InlineKeyboardMarkup(setting_b))

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "rename":
        await query.message.edit_text(
            text = "Your Rename Settings:",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("UPLOAD AS DOCUMENT", callback_data = "upload_as_doc"),
                        InlineKeyboardButton("APPLY CAPTION", callback_data = "ApplyDefaultCaption")
                    ]
                    [
                        InlineKeyboardButton("𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽", callback_data = "setCustomCaption"),
                        InlineKeyboardButton("𝚂𝙴𝚃 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻", callback_data = "setThumbnail")
                    ]
                    [
                        InlineKeyboardButton("MEGA EMAIL", callback_data = "megaemail"),
                        InlineKeyboardButton("MEGA PASSWORD", callback_data = "megapass"),
                   ]
                ]
            )
        )
        
                        
""""""""""" @Bot.on_message(filters.command("settings") & filters.private) 
async def show_settings(client: Client, message: Message):
    usr_id = message.chat.id
    user_data = db.get_user_data(usr_id)
    if not user_data:
        await message.reply_text("Failed to fetch your data from database!")
        return
    upload_as_doc = user_data.get("upload_as_doc", False)
    caption = user_data.get("caption", None)
    apply_caption = user_data.get("apply_caption", False)
    thumbnail = user_data.get("thumbnail", None)
    buttons_markup = [
        [types.InlineKeyboardButton(f"𝚄𝙿𝙻𝙾𝙰𝙳𝙴𝙳 𝙰𝚂 𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃 {'✅' if upload_as_doc else '🗑️'}",
                                    callback_data="triggerUploadMode")],
        [types.InlineKeyboardButton(f"𝙰𝙿𝙿𝙻𝚈 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 {'✅' if apply_caption else '🗑️'}",
                                    callback_data="triggerApplyCaption")],
        [types.InlineKeyboardButton(f"𝙰𝙿𝙿𝙻𝚈 𝙳𝙴𝙵𝙰𝚄𝙻𝚃 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 {'🗑️' if caption else '✅'}",
                                    callback_data="triggerApplyDefaultCaption")],
        [types.InlineKeyboardButton("𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽",
                                    callback_data="setCustomCaption")],
        [types.InlineKeyboardButton(f"{'𝙲𝙷𝙰𝙽𝙶𝙴' if thumbnail else '𝚂𝙴𝚃'} 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻",
                                    callback_data="setThumbnail")]
    ]
    if thumbnail:
        buttons_markup.append([types.InlineKeyboardButton("𝚂𝙷𝙾𝚆 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻",
                                                          callback_data="showThumbnail")])
    if caption:
        buttons_markup.append([types.InlineKeyboardButton("𝚂𝙷𝙾𝚆 𝙲𝙰𝙿𝚃𝙸𝙾𝙽",
                                                          callback_data="showCaption")])
    buttons_markup.append([types.InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴",
                                                      callback_data="closeMessage")])

    try:
        await m.edit(
            text="**- 𝙲𝚄𝚂𝚃𝙾𝙼𝙸𝚉𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂 -**",
            reply_markup=types.InlineKeyboardMarkup(buttons_markup),
            disable_web_page_preview=True,
            parse_mode="Markdown"
        )
    except errors.MessageNotModified: pass
    except errors.FloodWait as e:
        await asyncio.sleep(e.x)
        await show_settings(m)
    except Exception as err:
        Config.LOGGER.getLogger(__name__).error(err) """""""""""
