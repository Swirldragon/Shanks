from pyrogram import Client, filters
from pyrogram.types import Message
from pypdf import PdfReader, PdfWriter
from io import BytesIO
from bot import Bot

@Bot.on_message(filters=filters.command(['decryptpdf']))
async def decrypt_pdf(client: Client, message: Message):
    reply = message.reply_to_message
    if reply.document == None:
        await message.reply("Please reply to a PDF file with the /decryptPDF command.")
        
    else:
        pdf_file = await client.download_media(message.reply_to_download)
        pdf_reader = PdfReader(pdf_file)
        
        # Ask for password
        await message.reply("Please enter the password to decrypt the PDF file. Type `/cancel` to cancel.")
        password_message = await client.wait_for_message(chat_id=message.chat.id)
        
        if password_message.text == "/cancel":
            await message.reply("Decryption process cancelled.")
            return
        
        password = password_message.text
        
        # Decrypt the PDF file
        pdf_writer = PdfWriter()
        for page in range(pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page)
            pdf_writer.addPage(page_obj)
        pdf_writer.decrypt(password)
        
        # Create a BytesIO object to store the decrypted PDF
        decrypted_pdf = BytesIO()
        pdf_writer.write(decrypted_pdf)
        decrypted_pdf.seek(0)
        
        # Ask for new file name
        await message.reply("Please enter a new file name for the decrypted PDF file. Type `/cancel` to cancel.")
        filename_message = await client.wait_for_message(chat_id=message.chat.id)
        
        if filename_message.text == "/cancel":
            await message.reply("Decryption process cancelled.")
            return
        
        filename = filename_message.text + ".pdf"
        
        # Reply to the original message with the decrypted PDF
        await message.reply_to_message.reply_document(decrypted_pdf, file_name=filename)
    
