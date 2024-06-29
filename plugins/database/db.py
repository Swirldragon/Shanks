import pymysql
from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message

ADMINS = 1880221341

# Create a MySQL connection
cnx = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="shanks-justatestsubject-c98a.h.aivencloud.com",
    password="AVNS_uxSiv4oYViwH83p8Lbe",
    read_timeout=timeout,
    port=26463,
    user="avnadmin",
    write_timeout=timeout,
)

cursor = conn.cursor()

# Create the users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT,
        user_id INT,
        thumbnail BLOB,
        file_caption VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        PRIMARY KEY (id)
    );
""")
cnx.commit()

@Bot.on_message(filters.private & filters.command('view_data') & filters.user(ADMINS))
async def view_data(client, message):
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    output = "Saved Data:\n"
    for row in results:
        output += f"User ID: {row['user_id']}\n"
        output += f"Thumbnail: {row['thumbnail']}\n"
        output += f"File Caption: {row['file_caption']}\n"
        output += f"Email: {row['email']}\n"
        output += f"Password: {row['password']}\n\n"
    await message.reply(output)
