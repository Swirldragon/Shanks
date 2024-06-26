import telegram

# Create a Telegram bot instance
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Set up logging to a Telegram chat
logging_chat_id = 'YOUR_LOGGING_CHAT_ID'
bot.send_message(chat_id=logging_chat_id, text='Bot started')

# Handle updates
def handle_update(update):
    bot.send_message(chat_id=logging_chat_id, text=f'Received update: {update}')

bot.start_polling()
