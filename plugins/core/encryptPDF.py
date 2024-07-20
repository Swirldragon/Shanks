from pyrogram.types import Message
from pyrogram import Client, filters
import fitz
from bot import Bot 

async def encrypt_pdf(client, message):
    reply = message.reply_to_message
    if reply:
        pdf_file = await client.download_media(reply.document)

        password_message = await client.ask(chat_id = message.from_user.id, text = "Please enter a password to encrypt the PDF file. Type `/cancel` to cancel.", timeout=60)
        
        if password_message.text == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        password = password_message.text
        
        # Ask for new file name
        filename_message = await client.ask(chat_id = message.from_user.id, text = "Please enter a new file name for the encrypted PDF file. Type `/cancel` to cancel.", timeout=60)
        
        if filename_message.text == "/cancel":
            await message.reply("Encryption process cancelled.")
            return
        
        filename = filename_message.text
        
        try:
            # Encrypt the PDF file
            with fitz.open(pdf_file) as iNPUT:
                number_of_pages = iNPUT.page_count
                iNPUT.save(
                    enpdf,
                    encryption=fitz.PDF_ENCRYPT_AES_256,  # strongest algorithm
                    owner_pw=auth,
                    user_pw=f"{password}",
                    permissions=int(
                        fitz.PDF_PERM_ACCESSIBILITY
                        | fitz.PDF_PERM_PRINT
                        | fitz.PDF_PERM_COPY
                        | fitz.PDF_PERM_ANNOTATE
                    )
                )
            return True, output_path
            
        except Exception as Error:
            await message.reply_text("🐞 %s: %s" % (file_name, Error), exc_info=True)
            return False, Error

        
        await bot.send_document(message.from_user.id, document=enpdf, file_name=filename)

    
    else:
        await message.reply_text("Please reply to a PDF file with the /encryptPDF command.")
      
