from pyrogram import Client, filters
from pyrogram.types import Message
import os
import zipfile
import PyPDF2
from PIL import Image
from bot import bot
from datetime import datetime

p2c_operation = {}
c2p_operation = {}

@Bot.on_message(filters=filters.command(["p2c"]))
async def convert_pdf_to_cbz(client: Client, message: Message):
    user_id = message.from_user.id
    if message.reply_to_message:
        reply = message.reply_to_message
        media = reply.document
        filename = media.file_name
        file_id = media.file_id

        if file_id in renaming_operations:
            elapsed_time = (datetime.now() - renaming_operations[file_id]).seconds
            if elapsed_time < 10:
                print("File is being ignored as it is currently being renamed or was renamed recently.")
                return # Exit the handler if the file is being ignored
                
         # Mark the file as currently being renamed
        p2c_operations[file_id] = datetime.now()
            
        file = await client.download_media(media)
        await message.reply("Downloading....")
        await asyncio.sleep(10)
            
        pdf_file = open(file, "rb")
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = pdf_reader.numPages
        images = []
            
        for page in range(num_pages):
            page_obj = pdf_reader.getPage(page)
            image = page_obj.convert("JPEG")
            images.append(image)
        cbz_file = zipfile.ZipFile("filename.cbz", "w")
        
        await message.reply_text("Uploading........")
        await asyncio.sleep(10)
        
        for i, image in enumerate(images):
            image.save(f"page_{i+1}.jpg", "JPEG")
            cbz_file.write(f"page_{i+1}.jpg")
        cbz_file.close()
        await client.send_document(user_id, "filename.cbz")
            
    else:
        await message.reply("Please send a PDF file with reply.")

@Bot.on_message(filters=filters.command(["p2c"]))
async def convert_cbz_to_pdf(self, client, message):
    user_id = message.from_user.id
    if message.reply_to_message:
        reply = message.reply_to_message.document
        file_id = reply.file_id
        filename = reply.file_name
        
        if file_id in renaming_operations:
            elapsed_time = (datetime.now() - renaming_operations[file_id]).seconds
            if elapsed_time < 10:
                print("File is being ignored as it is currently being renamed or was renamed recently.")
                return # Exit the handler if the file is being ignored
                
         # Mark the file as currently being renamed
        c2p_operations[file_id] = datetime.now()
        
        file = await client.download_media(message.reply_to_message)
        await message.reply_text("Downloading........")
        await asyncio.sleep(10)
        
        cbz_file = zipfile.ZipFile(file, "r")
        images = []
        for name in cbz_file.namelist():
            if name.endswith(".jpg"):
                image = Image.open(cbz_file.extract(name))
                images.append(image)
        pdf_file = open("filename.pdf", "wb")
        pdf_writer = PyPDF2.PdfWriter(pdf_file)
        
        await message.reply_text("Uploading........")
        await asyncio.sleep(10)
        
        for image in images:
            image.save("temp.jpg", "JPEG")
            pdf_writer.addPage(PyPDF2.PdfReader("temp.jpg").getPage(0))
        pdf_file.close()
        os.remove("temp.jpg")
        await client.send_document(user_id, "filename.pdf")
    else:
        await message.reply("Please send a CBZ file with reply.")
