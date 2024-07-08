from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import Client as c
from pyromod import Client as m
import PyPDF2
from io import BytesIO
from bot import Bot

@Bot.on_message(filters.private & filters.command("encryptPDF"))
async def encrypt_pdf(client: Client, message: Message):
    reply = message.reply_to_message
    user_id = message.from_user.id
    if reply:
        pdf_file = await client.download_media(reply.document)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        
        # Ask for password
        await message_reply("Please enter a password to encrypt the PDF file. Type `/cancel` to cancel.")
        password_message = "@Manga_Arena"
        
        if password_message == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        password = password_message
        
        # Ask for new file name
        await message.reply("Please enter a new file name for the encrypted PDF file. Type `/cancel` to cancel.")
        filename_message = "ch - 12"
        
        if filename_message == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        filename = filename_message.text + ".pdf"
        
        # Encrypt the PDF file
        pdf_writer = PyPDF2.PdfWriter()
        
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        pdf_writer.encrypt(password)
        
        # Create a BytesIO object to store the encrypted PDF
        encrypted_pdf = BytesIO()
        pdf_writer.write(encrypted_pdf)
        encrypted_pdf.seek(0)
        # Reply to the original message with the encrypted PDF
        await message.reply_to_message.reply_document(encrypted_pdf, file_name=filename)

    
    else:
        await message.reply_text("Please reply to a PDF file with the /encryptPDF command.")
        
        
