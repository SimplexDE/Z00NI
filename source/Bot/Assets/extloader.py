from ..commands.Assets.dev import load
from loguru import logger

def extloader(self, extensions: list):
    logger.debug("Lade eingetragene Extensions...")
    for _extension in extensions:
        try:
            self.load_extension(f"source.Bot.commands.{_extension}")
            result = True
        except Exception as e:
            logger.error(f"Fehler beim Laden von {_extension.upper()}")
            logger.error(e)
            result = False
        if result == True:
            logger.debug(f"{_extension.upper()} geladen")
        elif result == False:
            logger.debug(f"{_extension.upper()} nicht geladen")
    logger.debug("Abgeschlossen.")
    
