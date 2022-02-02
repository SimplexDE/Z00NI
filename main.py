from loguru import logger
import os

from source.Bot import bot

version = os.getenv("version")

bot.start(version)
