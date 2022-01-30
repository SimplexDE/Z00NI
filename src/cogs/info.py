import nextcord
from nextcord.ext import commands
import asyncio
from src.helper.checks import is_staff


class info(commands.Cog):
	"""Informational commands"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="ping")
	async def ping(self, ctx):
		"""Responds with pong(WIP: websocket & api latency response)"""
		await ctx.send("Pong")


def setup(bot):
	bot.add_cog(info(bot))
