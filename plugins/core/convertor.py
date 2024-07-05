from pyrogram import Client, filters
from pyrogram.types import Message
import os
import zipfile
import PyPDF2
from PIL import Image
from bot import Bot

@Bot.on_message(filters=filters.command(['p2c'])) 
async def convert_pdf_to_cbz(client: Client, message: Message):
    if message.reply_to_message == True:
        file_id = message.document.file_id
        file = await client.download_media(message.reply_to_message)
        pdf_file = open(file, "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages
        images = []
        for page in range(num_pages):
            page_obj = pdf_reader.getPage(page)
            image = page_obj.convert("JPEG")
            images.append(image)
        cbz_file = zipfile.ZipFile("output.cbz", "w")
        for i, image in enumerate(images):
            image.save(f"page_{i+1}.jpg", "JPEG")
            cbz_file.write(f"page_{i+1}.jpg")
        cbz_file.close()
        await client.send_document(message.chat.id, "output.cbz")
    else:
        await message.reply("Please send a PDF file.")

@Bot.on_message(filters=filters.command(['c2p'])) 
async def convert_cbz_to_pdf(client, message):
    if message.reply_to_message == True:
        file_id = message.document.file_id
        file = await client.download_media(message.reply_to_message)
        cbz_file = zipfile.ZipFile(file, "r")
        images = []
        for name in cbz_file.namelist():
            if name.endswith(".jpg"):
                image = Image.open(cbz_file.extract(name))
                images.append(image)
        pdf_file = open("output.pdf", "wb")
        pdf_writer = PyPDF2.PdfFileWriter()
        for image in images:
            pdf_writer.addPage(image)
        pdf_writer.write(pdf_file)
        pdf_file.close()
        await client.send_document(message.chat.id, "output.pdf")
    else:
        await message.reply("Please send a CBZ file.")
