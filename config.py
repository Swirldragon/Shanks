import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

#Bot token @Botfather
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5170934938:AAHWTgb6FH676fzS-JI3lxxomESplXS8ai0")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", 20631875)

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e770f81e0d2f21d48f738c010a51fd6e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001550448024"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1880221341"))

#Port
PORT = os.environ.get("PORT", "8080")

LOG_FILE_NAME = "renamerbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
