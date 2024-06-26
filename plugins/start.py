from pyrogram import Client, filters
from pyrogram.types import Message

photos = [
    "https://graph.org/file/e93290b99f1a87211ee7c.jpg",
    "https://graph.org/file/ccf9d8a22e8220990850d.jpg",
    "https://graph.org/file/5e9f4d6b735a19e973d12.jpg",
    "https://graph.org/file/8cc2e4d1ccf20ecec6d8b.jpg",
    "https://graph.org/file/342f8b723a35dfbb2d2b5.jpg",
    "https://graph.org/file/ef3c23fa7f07d2078e2c9.jpg",
    "https://graph.org/file/e358de4b9807c4c5a1cd6.jpg",
    "https://graph.org/file/4523cccaf531c8fcbdc79.jpg"
]

@app.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
  pass
