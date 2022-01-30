import os
import nextcord
from loguru import logger


def launch(self):
    """Bot Launch"""

    loaded_cmds = 0
    not_loaded_cmds = 0

    from src.helper.keep_alive import keep_alive

    keep_alive()

    # from src.helper.sentryio import start_sentryio

    # start_sentryio()

    @self.event
    async def on_ready():
        #print(f"\nEingeloggt als {{0.user}}, mit Nextcord {{1.__version__}}\nEs wurde/n {{2}} Cog/s geladen.\nEs wurde/n {{3}} Cog/s ausgelassen".format(bot, nextcord, loaded_cmds, not_loaded_cmds))
        logger.success("Bot Funktionsbereit.")
        logger.info(f"Eingeloggt als {self.user} / {self.user.id}")
        logger.info(f"Nextcord Version: {nextcord.__version__}")
        logger.info(f"Python Version: 3.9.7")

    os.chdir("src/")

    for filename in os.listdir("cogs/"):
        if filename.startswith("-"):
            not_loaded_cmds += 1
            pass
        elif filename.endswith(".py"):
            self.load_extension(f'src.cogs.{filename[:-3]}')
            logger.info(f"{filename[:-3].upper()} geladen")
            loaded_cmds += 1
