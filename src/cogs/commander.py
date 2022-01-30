import nextcord
from nextcord.ext import commands
import asyncio
from src.functions.commanderfunctions import load, unload, reload
from src.helper.checks import is_dev

timeout = 2


class commander(commands.Cog):
	"""Cog-Managment"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="load")
	@is_dev()
	async def load(self, ctx, command):
		"""Loads a cog"""
		#msg = await ctx.send("...")
		result = await load(self.bot, ctx, command)
		#await msg.edit(result, delete_after=timeout)

	@commands.command(name="unload")
	@is_dev()
	async def unload(self, ctx, command):
		"""Unloads a cog"""
		#msg = await ctx.send("...")
		result = await unload(self.bot, ctx, command)
		##await msg.edit(result, delete_after=timeout)

	@commands.command(name="reload")
	@is_dev()
	async def reload(self, ctx, command):
		"""Reloads a cog"""
		#msg = await ctx.send("...")
		result = await reload(self.bot, ctx, command)
		#await msg.edit(result, delete_after=timeout)


def setup(bot):
	bot.add_cog(commander(bot))
