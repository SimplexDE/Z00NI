import os
from nextcord.ext import commands
import json
from src.__launcher__ import launch

with open('../configuration.json', 'r') as f:
	data = json.load(f)

	token = data["TOKEN"]
	tokendev = data["TOKEN_DEV"]

bot = commands.Bot(command_prefix="!",
					case_insensitive=False,
					description="Simplex Utilies / Developed by Simplex#7008")

launch(bot)

bot.run(token)
