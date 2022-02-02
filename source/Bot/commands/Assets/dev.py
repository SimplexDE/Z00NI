from loguru import logger

def load(self, module):
    try:
        self.bot.load_extension(f"source.Bot.commands.{module}")
        logger.debug(f"{module.upper()} wird geladen...")
    except Exception as e:
        logger.error(f"Fehler beim laden von {module.upper()}")
        logger.error(e)
        return False
    else:
        logger.debug(f"{module.upper()} geladen.")
        return True

def unload(self, module):
    try:
        self.bot.unload_extension(f"source.Bot.commands.{module}")
        logger.debug(f"{module.upper()} wird entladen...")
    except Exception as e:
        logger.error(f"Fehler beim entladen von {module.upper()}")
        logger.error(e)
        return False
    else:
        logger.debug(f"{module.upper()} entladen.")
        return True

def reload(self, module):
    try:
        self.bot.reload_extension(f"source.Bot.commands.{module}")
        logger.debug(f"{module.upper()} wird neugeladen...")
    except Exception as e:
        logger.error(f"Fehler beim neuladen von {module.upper()}")
        logger.error(e)
        return False
    else:
        logger.debug(f"{module.upper()} neugeladen.")
        return True
