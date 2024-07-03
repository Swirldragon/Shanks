from PyPDF2 import PdfFileReader, PdfFileWriter
from io import BytesIO
from bot import Bot

async def decrypt_pdf(client, message):
    # Check if the user sent a PDF file
    replied_message = message.reply_to_message
    document = replied_message.document
    if document == True:
        pdf_file = await client.download_media(message.reply_to_message)
        pdf_reader = PdfFileReader(pdf_file)
        
        # Ask for password
        await message.reply("Please enter the password to decrypt the PDF file. Type `/cancel` to cancel.")
        password_message = await client.wait_for_message(chat_id=message.chat.id)
        
        if password_message.text == "/cancel":
            await message.reply("Decryption process cancelled.")
            return
        
        password = password_message.text
        
        # Decrypt the PDF file
        pdf_writer = PdfFileWriter()
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
    else:
        await message.reply("Please reply to a PDF file with the /decryptPDF command.")
