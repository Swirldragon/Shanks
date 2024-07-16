from bot import Bot
from aiohttp import web
from plugins import web_server

#web-response
app = web.AppRunner(await web_server())
await app.setup()
bind_address = "0.0.0.0"
await web.TCPSite(app, bind_address, PORT).start()

Bot.run()
