import nextcord
from nextcord.ext import commands
import asyncio
from loguru import logger


class fun(commands.Cog):
	"""Commands for the funsies"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="calc")
	#@is_staff()
	async def calc(self, ctx, int1: int, operator, int2: int):
		"""Calcuator"""
		logger.debug(f"CALC aufgerufen von: {ctx.author.name}#{ctx.author.discriminator}")
		if operator == "+":
			result = int1 + int2
		elif operator == "-":
			result = int1 - int2
		elif operator == "*":
			result = int1 * int2
		elif operator == "/":
			if int1 == 0:
				if int2 == 0:
					result = False
					await ctx.send(result)
					return False
			result = int1 / int2
		await ctx.send(result)
		return True


def setup(bot):
	bot.add_cog(fun(bot))
