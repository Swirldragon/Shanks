from bot import LOG_CHANNEL
from .db import db
from pyrogram import Client
from pyrogram.types import Message


async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if LOG_CHANNEL is not None:
            await bot.send_flooded_message(
                int(LOG_CHANNEL),
                f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{(await bot.get_me()).username} !!"
            )
