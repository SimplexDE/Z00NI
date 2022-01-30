import os
from nextcord.ext import commands
import json
from loguru import logger
from src.__launcher__ import launch

with open('../configuration.json', 'r') as f:
	data = json.load(f)

	token = data["TOKEN"]
	tokendev = data["TOKEN_DEV"]

bot = commands.Bot(command_prefix="!",
					case_insensitive=False,
					description="Simplex Utilies / Developed by Simplex#7008")

logger.info("Bot wird gestartet.")
try:
	launch(bot)
except Exception as e:
	logger.critical(f"Bot konnte nicht gestartet werden!")
	logger.critical(e)
else:
	logger.success("Bot gestartet.")

bot.run(token)
