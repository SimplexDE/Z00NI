import os
from time import strftime

from loguru import logger
from nextcord.ext import commands

from .Helper.keep_alive import keep_alive

bot = commands.Bot(command_prefix="d!", case_insensitive=False)

def start(version):
    try:
        timeformat = "%d.%m.%Y, %H:%M:%S"
        bot = commands.Bot(command_prefix="d!", case_insensitive=False)

        logger.level("SYSTEM", no=60, color="<red>", icon="🚨")
        logger.level("BOT", no=25, color="<blue>", icon="🤖")

        logger.log("SYSTEM", f"System startet... | Version: {version}, {strftime(timeformat)}")

        bot.load_extension(f"source.Bot.commands.developer")

        # TODO: Extension Loader hier

        keep_alive()

        bot.run(os.getenv("tokendev"))
    except Exception as e:
        logger.critical(f"Kritischer Fehler. System konnte nicht gestartet werden!")
        logger.critical(e)
        return False
    else:
        return True

async def stop(ctx):
    try:
        logger.critical("SHUTDOWN INITIATED")
        await ctx.send("*Sleepmode activated...*")
        #await bot.change_presence(activity=None, status=nextcord.Status.offline) # BUG FIXME: Will nicht funktionieren.. Irgendwann mal fixxen.
    except Exception as e:
        logger.critical("Kritischer Fehler. System konnte nicht gestoppt werden!")
        logger.critical(e)
        return False
    else:
        return exit()
