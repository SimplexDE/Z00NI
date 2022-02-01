from datetime import datetime
import os
from time import strftime

from Helper.keep_alive import keep_alive
from loguru import logger
from nextcord.ext import commands


def start(version):
    try:
        timeformat = "%d.%m.%Y, %H:%M:%S"
        bot = commands.Bot(command_prefix="d!", case_insensitive=False)
        logger.level("SYSTEM", no=60, color="<red>", icon="🚨")
        logger.log("SYSTEM", f"System startet... | Version: {version}, {strftime(timeformat)}")
        keep_alive()
        bot.run(os.getenv("tokendev"))
    except Exception as e:
        logger.critical(f"Kritischer Fehler. System konnte nicht gestartet werden!")
        logger.critical(e)
        return False
    else:
        return True

def stop():
    try:
        logger.log("SYSTEM", "Dieser Befehl ist noch nicht fertig.")
    except Exception as e:
        logger.critical("Kritischer Fehler. System konnte nicht gestoppt werden!")
        logger.critical(e)
        return False
    else:
        return True
    
# bot = commands.Bot(command_prefix="d!",
# 					case_insensitive=False,
# 					description="Z00NI / Developed by Simplex#7008")

# logger.level("STARTUP", no=10, color="<magenta>")

# logger.log("STARTUP", "Bot wird gestartet.")

# try:
# 	loaded_cmds = 0
# 	not_loaded_cmds = 0

# 	from src.helper.keep_alive import keep_alive

# 	keep_alive()

# 	# from src.helper.sentryio import start_sentryio

# 	# start_sentryio()

# 	logger.add("Logs/DEBUG_{time}.log", level="DEBUG", rotation="200 MB", delay=True, retention="1 hour", compression="zip")
# 	logger.add("Logs/WARNING_{time}.log", level="WARNING", rotation="100 MB", delay=True, retention="1.5 hour", compression="zip")
# 	logger.add("Logs/ERROR_{time}.log", level="ERROR", rotation="100 MB", delay=True, retention="2 hour", compression="zip")
# 	logger.add("Logs/CRITICAL_{time}.log", level="CRITICAL", rotation="100 MB", delay=True, retention="3 hour", compression="zip")

# 	@bot.event
# 	async def on_ready():
# 		#print(f"\nEingeloggt als {{0.user}}, mit Nextcord {{1.__version__}}\nEs wurde/n {{2}} Cog/s geladen.\nEs wurde/n {{3}} Cog/s ausgelassen".format(bot, nextcord, loaded_cmds, not_loaded_cmds))
# 		logger.success("Bot Funktionsbereit.")
# 		logger.info(f"Eingeloggt als {bot.user} / {bot.user.id}")
# 		logger.info(f"Nextcord Version: {__version__}")
# 		logger.info(f"Python Version: 3.9.7")

# 	os.chdir("src/")

# 	for filename in os.listdir("cogs/"):
# 		if filename.startswith("-"):
# 			not_loaded_cmds += 1
# 			pass
# 		elif filename.endswith(".py"):
# 			bot.load_extension(f'src.cogs.{filename[:-3]}')
# 			logger.info(f"{filename[:-3].upper()} geladen")
# 			loaded_cmds += 1	
# except Exception as e:
# 	logger.critical(f"Bot konnte nicht gestartet werden!")
# 	logger.critical(e)
# 	logger.log("STARTUP", "Start wurde abgebrochen.")
# 	bot.logout()
# else:
# 	logger.log("STARTUP", "Bot gestartet.")

# bot.run(os.getenv("tokendev"))
