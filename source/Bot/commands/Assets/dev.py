from loguru import logger

async def load(self, module):
    try:
        self.bot.load_extension(f"source.Bot.commands.{module}")
    except Exception as e:
        logger.error(f"Fehler beim laden von {module.upper()}")
        logger.error(e)
        return False
    else:
        return True

async def unload(self, module):
    try:
        self.bot.unload_extension(f"source.Bot.commands.{module}")
    except Exception as e:
        logger.error(f"Fehler beim entladen von {module.upper()}")
        logger.error(e)
        return False
    else:
        return True

async def reload(self, module):
    try:
        self.bot.reload_extension(f"source.Bot.commands.{module}")
    except Exception as e:
        logger.error(f"Fehler beim neuladen von {module.upper()}")
        logger.error(e)
        return False
    else:
        return True
