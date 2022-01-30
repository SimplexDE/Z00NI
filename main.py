import os
from nextcord.ext import commands
from src.__launcher__ import launch

bot = commands.Bot(command_prefix="!",
					case_insensitive=False,
					description="Simplex Utilies / Developed by Simplex#7008")

launch(bot)

bot.run(os.getenv("token"))
