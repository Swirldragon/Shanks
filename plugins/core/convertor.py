from pyrogram import Client, filters
from pyrogram.types import Message
import os
import zipfile
from fpdf import FPDF
from PIL import Image
from datetime import datetime
import asyncio
import time
from bot import Bot

p2c_operation = {}
c2p_operation = {}

""" async def convert_pdf_to_cbz(client: Client, message: Message):
    user_id = message.from_user.id
    if message.reply_to_message:
        reply = message.reply_to_message
        media = reply.document
        filename = media.file_name
        file_id = media.file_id

        if file_id in p2c_operation:
            elapsed_time = (datetime.now() - p2c_operation[file_id]).seconds
            if elapsed_time < 10:
                print("File is being ignored as it is currently being renamed or was renamed recently.")
                return # Exit the handler if the file is being ignored
                
         # Mark the file as currently being renamed
        p2c_operation[file_id] = datetime.now()
            
        file = await client.download_media(media)
        await message.reply("Downloading....")
        await asyncio.sleep(6)
            
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
        await asyncio.sleep(6)
        
        for i, image in enumerate(images):
            image.save(f"page_{i+1}.jpg", "JPEG")
            cbz_file.write(f"page_{i+1}.jpg")
        cbz_file.close()
        await client.send_document(user_id, "filename.cbz")
            
    else:
        await message.reply("Please send a PDF file with reply.") """


async def convert_cbz_to_pdf(bot, message):
    user_id = message.from_user.id
    if message.reply_to_message:
        reply = message.reply_to_message
        file = reply.document
        start_time = time.time()
        file_name = file.file_name
        file_id = file.file_id
        try:
            new_file = await bot.get_messages('me', file_id)
            file_path = f"{file_name}/{user_id}.cbz"

            # Inform user that download is starting
            i1 = await message.reply_text("<code>Downloading the file, please wait...</code>")

            # Download the file
            await new_file.download(file_path)

            # Inform user that extraction is starting
            i2 = await message.reply_text("<code>File downloaded. Extracting images...</code>")
            i1.delete()

            # Extract the .cbz file
            extract_path = file_id
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            # Create a PDF from extracted images
            pdf = FPDF()
            supported_extensions = ('.jpg', '.jpeg', '.png', '.gif')
            image_files = []
            for root, _, files in os.walk(extract_path):
                for name in files:
                    if name.lower().endswith(supported_extensions):
                        image_files.append(os.path.join(root, name))

            # Sort image files based on their filenames
            image_files.sort()

            for image in image_files:
                pdf.add_page()

                with Image.open(image) as img:
                    width, height = img.size
                    aspect_ratio = height / width
                    pdf_width = 210
                    pdf_height = pdf_width * aspect_ratio
                    if pdf_height > 297:
                        pdf_height = 297
                        pdf_width = pdf_height / aspect_ratio

                    x = (210 - pdf_width) / 2  # Center horizontally
                    y = (297 - pdf_height) / 2  # Center vertically

                    pdf.image(image, x=x, y=y, w=pdf_width, h=pdf_height)

            pdf_output_path = f"{file_name}.pdf"
            pdf.output(pdf_output_path)

            # Inform user that PDF creation is complete
            end_time = time.time()
            total_time = end_time - start_time

            # Send the PDF file
            with open(pdf_output_path, 'rb') as f:
                await bot.send_document(chat_id=user_id, document=f)
                await message.reply_text(f'Extraction and PDF creation complete. Conversion time: {total_time:.2f} seconds.')

            # Clean up
            os.remove(file_path)
            os.remove(pdf_output_path)
            for root, _, files in os.walk(extract_path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                os.rmdir(root)

        except Exception as e:
            await message.reply_text(f'An error occurred: {e}')
    else:
        await message.reply_text('Please send a valid .cbz file.')
