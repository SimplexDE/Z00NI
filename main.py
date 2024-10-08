import os
from nextcord.ext import commands
import json
from loguru import logger
from src.__launcher__ import launch

bot = commands.Bot(command_prefix="d!",
					case_insensitive=False,
					description="Z00NI / Developed by Simplex#7008")

STARTUP = logger.level("STARTUP", no=40, color="<magenta>")

logger.log("STARTUP", "Bot wird gestartet.")
try:
	launch(bot)
except Exception as e:
	logger.critical(f"Bot konnte nicht gestartet werden!")
	logger.critical(e)
	logger.log("STARTUP", "Start wurde abgebrochen.")
	bot.logout()
else:
	logger.log("STARTUP", "Bot gestartet.")

bot.run(os.getenv("token"))
