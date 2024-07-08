from pyromod import Client, Message
from pyrogram.types import Message as M
from pyrogram import Client as C
import PyPDF2
from io import BytesIO

@Client.on_message(filters.command("encryptPDF"))
async def encrypt_pdf(client: Client, message: Message, M, C):
    reply = M.reply_to_message
    if reply:
        pdf_file = await C.download_media(reply.document)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        
        # Ask for password
        password_a = await chat.ask("Please enter a password to encrypt the PDF file. Type `/cancel` to cancel.")
        password_message = password_a.text
        
        if password_message.text == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        password = password_message
        
        # Ask for new file name
        filename_a = await chat.ask("Please enter a new file name for the encrypted PDF file. Type `/cancel` to cancel.")
        filename_message = filename_a.text
        
        if filename_message.text == "/cancel":
            await M.reply("Encryption process cancelled.")
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
        await M.reply_to_message.reply_document(encrypted_pdf, file_name=filename)

    
    else:
        await message.reply_text("Please reply to a PDF file with the /encryptPDF command.")
        
        
