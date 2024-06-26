
if __name__ == '__main__':
    threading.Thread(target=run_server).start()
    bot.infinity_polling()
