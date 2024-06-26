from pyrogram import Client, filters
from pyrogram.types import Message
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Initialize Pyrogram client
app = Client("my_bot", api_id=12345, api_hash="your_api_hash", bot_token="your_bot_token")

# Define a function to run the web server
def run_server():
    APP_HOST = ''
    APP_PORT = int(os.environ.get('PORT'))
    class GetHandler(BaseHTTPRequestHandler):
        def _set_headers(self):
            self.send_response(204)
            self.end_headers()

        def do_GET(self):
            self._set_headers()

    server_address = (APP_HOST, APP_PORT)
    httpd = HTTPServer(server_address, GetHandler)
    httpd.serve_forever()

# Define a function to handle the /status command
@app.on_message(filters.command("status") & filters.user("your_owner_id"))
async def status_handler(client, message: Message):
    # Get the current bot status
    status = await client.get_me()

    # Send a response to the owner
    await message.reply(f"Bot status: {status.first_name} ({status.username})")

# Run the web server in a separate thread
threading.Thread(target=run_server).start()

# Start the Pyrogram client
app.run()
