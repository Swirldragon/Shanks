import loguru

loguru.logger.add('telegram_bot.log', level='INFO')

# Create a Telegram bot instance
bot = telegram.Bot(token='5170934938:AAHWTgb6FH676fzS-JI3lxxomESplXS8ai0')

# Log a message
loguru.logger.info('Bot started')

# Handle updates
def handle_update(update):
    loguru.logger.info(f'Received update: {update}')

bot.start_polling()
