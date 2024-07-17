from pyrogram.types import Message
from pyrogram import Client, filters
from pypdf import PdfReader, PdfWriter
from io import BytesIO
from bot import Bot 

async def encrypt_pdf(client: Client, message: Message):
    reply = message.reply_to_message
    if reply:
        pdf_file = await client.download_media(reply.document)
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        
        password_message = await client.ask("Please enter a password to encrypt the PDF file. Type `/cancel` to cancel.")
        
        if password_message.text == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        password = password_message.text
        
        # Ask for new file name
        filename_message = await client.ask("Please enter a new file name for the encrypted PDF file. Type `/cancel` to cancel.")
        
        if filename_message.text == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        filename = filename_message.text
        
        # Encrypt the PDF file
        pdf_writer = PdfWriter()
        
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
        


@Bot.on_message(filters=filters.command(["encryptPDF"]))
async def handle_encrypt_pdf(client: Client, message: Message):
    await encrypt_pdf(client, message)
