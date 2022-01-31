from nextcord.ext import commands
import nextcord
from loguru import logger
from src.helper.checks import is_bot, is_dev



class logger_(commands.Cog):
	"""Logger"""
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_command_error(self, ctx, e):
		logger.error(f"Bei der Ausführung eines Commands ist ein Fehler aufgetreten!")
		logger.error(f"{e}")
		await ctx.send("Fehler du Dummkopf!")

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == 881186799538540565:
			return False
		ch = self.bot.get_channel(937341847800541196)
		if message.channel == ch:
			await message.delete()
			return False

	@commands.Cog.listener()
	async def on_message_edit(self, message, message_new):
		if message.author.id == 881186799538540565:
			return False
		if message.content.startswith("!"):
			return False
		ch = self.bot.get_channel(937341847800541196)
		if message.channel == ch:
			return False
		
		CONTENT_old = message.content
		CONTENT_new = message_new.content
		CHANNEL = message.channel
		CHANNELID = message.channel.id
		GUILD = message.guild.name
		GUILDID = message.guild.id
		AUTHOR_NAME = message.author.name
		AUTHOR_DISC = message.author.discriminator
		AUTHORID = message.author.id

		embed = nextcord.Embed(title=f":recycle: | Message Edited", description=f"Author: <@{AUTHORID}> `{AUTHOR_NAME}#{AUTHOR_DISC}`\nOld Content: `{CONTENT_old}`\nNew Content: `{CONTENT_new}`\nServer: `{GUILD}/{GUILDID}`\nChannel: <#{CHANNELID}> `{CHANNEL}/{CHANNELID}`")

		await ch.send(embed=embed)	

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		if message.author.id == 881186799538540565:
			return False
		if message.content.startswith("!"):
			return False
		ch = self.bot.get_channel(937341847800541196)
		if message.channel == ch:
			return False
		
		CONTENT = message.content
		CHANNEL = message.channel
		CHANNELID = message.channel.id
		GUILD = message.guild.name
		GUILDID = message.guild.id
		AUTHOR_NAME = message.author.name
		AUTHOR_DISC = message.author.discriminator
		AUTHORID = message.author.id

		embed = nextcord.Embed(title=f":wastebasket: | Message Deletion", description=f"Author: <@{AUTHORID}> `{AUTHOR_NAME}#{AUTHOR_DISC}`\nContent: `{CONTENT}`\nServer: `{GUILD}/{GUILDID}`\nChannel: <#{CHANNELID}> `{CHANNEL}/{CHANNELID}`")

		await ch.send(embed=embed)

def setup(bot):
	bot.add_cog(logger_(bot))