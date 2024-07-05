from pyrogram import Client, filters
import PyPDF2
from io import BytesIO
from bot import Bot

@Bot.on_message(filters.private & filters.command("encryptPDF"))
async def encrypt_pdf(client, message):
    # Check if the user sent a PDF file
    replied_message = message.reply_to_message
    document = replied_message.document
    if message.reply_to_message == True:
        pdf_file = await client.download_media(message.reply_to_message)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = pdf_reader.numPages
        
        # Ask for password
        await message.reply("Please enter a password to encrypt the PDF file. Type `/cancel` to cancel.")
        password_message = await client.wait_for_message(chat_id=message.chat.id)
        
        if password_message.text == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        password = password_message.text
        
        # Ask for new file name
        await message.reply("Please enter a new file name for the encrypted PDF file. Type `/cancel` to cancel.")
        filename_message = await client.wait_for_message(chat_id=message.chat.id)
        
        if filename_message.text == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        filename = filename_message.text + ".pdf"
        
        # Encrypt the PDF file
        pdf_writer = PyPDF2.PdfWriter()
        for page in range(num_pages):
            page_obj = pdf_reader.getPage(page)
            pdf_writer.addPage(page_obj)
        pdf_writer.encrypt(password)
        
        # Create a BytesIO object to store the encrypted PDF
        encrypted_pdf = BytesIO()
        pdf_writer.write(encrypted_pdf)
        encrypted_pdf.seek(0)
        
        # Reply to the original message with the encrypted PDF
        await message.reply_to_message.reply_document(encrypted_pdf, file_name=filename)
    else:
        await message.reply("Please reply to a PDF file with the /encryptPDF command.")
