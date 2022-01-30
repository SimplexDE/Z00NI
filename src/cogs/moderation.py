import nextcord
from nextcord.ext import commands
from src.helper.checks import is_staff


class moderation(commands.Cog):
	"""Work in Progress | Commands are locked to Staff"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="lock")
	@is_staff()
	async def lock(self, ctx, *args):
		reason = ""
		await ctx.message.delete()
		for _num, _arg in enumerate(args):
			if _arg.startswith("-r"):
				for _reason_arg in args[_num + 1:]:
					if _reason_arg.startswith("-"):
						break
					else:
						reason += _reason_arg + " "
		
		embed_locked = nextcord.Embed(title="")
		embed_unlocked = nextcord.Embed(title="")

		ch = self.bot.get_channel(ctx.message.channel.id)
		if ctx.guild.default_role not in ch.overwrites:
			overwrites = {
				ctx.guild.default_role: nextcord.PermissionOverwrite(send_messages=False)
            }
			await ch.edit(overwrites=overwrites)
			if reason == "":
				embed = nextcord.Embed(title=f":lock: | {ch.name} Locked.", colour=nextcord.Colour.red())
			else:
				embed = nextcord.Embed(title=f":lock: | {ch.name} Locked.", colour=nextcord.Colour.red(), description=f"Reason: {reason}")
		elif ch.overwrites[ctx.guild.default_role].send_messages == True or ch.overwrites[ctx.guild.default_role].send_messages == None:
			overwrites = ch.overwrites[ctx.guild.default_role]
			overwrites.send_messages = False
			await ch.set_permissions(ctx.guild.default_role, overwrite=overwrites)
			if reason == "":
				embed = nextcord.Embed(title=f":unlock: | {ch.name} Locked.", colour=nextcord.Colour.red())
			else:
				embed = nextcord.Embed(title=f":unlock: | {ch.name} Locked.", colour=nextcord.Colour.red(), description=f"Reason: {reason}")
		else:
			overwrites = ch.overwrites[ctx.guild.default_role]
			overwrites.send_messages = True
			await ch.set_permissions(ctx.guild.default_role, overwrite=overwrites)
			if reason == "":
				embed = nextcord.Embed(title=f":unlock: | {ch.name} Unlocked.", colour=nextcord.Colour.green())
			else:
				embed = nextcord.Embed(title=f":unlock: | {ch.name} Unlocked.", colour=nextcord.Colour.green(), description=f"Reason: `{reason}`")
		await ctx.send(embed=embed)
		

	@commands.command(name="purge")
	@is_staff()
	async def purge(self, ctx, amount: int, *args):
		reason = ""
		amount = amount
		await ctx.message.delete()
		for _num, _arg in enumerate(args):
			if _arg.startswith("-r"):
				for _reason_arg in args[_num + 1:]:
					if _reason_arg.startswith("-"):
						break
					else:
						reason += _reason_arg + " "
		await ctx.channel.purge(limit=amount)
		if reason == "":
			embed = nextcord.Embed(title=":fire: | Message Purge", colour=nextcord.Colour.orange(), description=f"Amount: `{amount}`")
		else:
			embed = nextcord.Embed(title=":fire: | Message Purge", colour=nextcord.Colour.orange(), description=f"Amount: `{amount}`\nReason: `{reason[:-1]}`")
		await ctx.send(embed=embed)

	@commands.command(name="case")
	@is_staff()
	async def case(self, ctx, *args):
		"""Work in Progress"""
		await ctx.message.delete()
		msg = await ctx.send("...")

	@commands.command(name="cases")
	@is_staff()
	async def cases(self, ctx, *args):
		"""Work in Progress"""
		await ctx.message.delete()
		msg = await ctx.send("...")

	@commands.command(name="ban")
	@is_staff()
	async def ban(self, ctx, *args):
		"""Work in Progress"""
		await ctx.message.delete()
		msg = await ctx.send("...")

	@commands.command(name="kick")
	@is_staff()
	async def kick(self, ctx, *args):
		"""Work in Progress"""
		await ctx.message.delete()
		msg = await ctx.send("...")

	@commands.command(name="mute")
	@is_staff()
	async def mute(self, ctx, *args):
		"""Work in Progress"""
		await ctx.message.delete()
		msg = await ctx.send("...")

	@commands.command(name="warn")
	@is_staff()
	async def warn(self, ctx, *args):
		"""Work in Progress"""
		await ctx.message.delete()
		msg = await ctx.send("...")
		args = list(args)
		finalArgs = []
		for _arg in list(args):
			if _arg.startswith("-"):
				if len(_arg) > 2:
					num = len(_arg) - 2
					_arg = _arg[:-num]
				finalArgs += _arg[1:]
		await msg.edit(finalArgs)

		args = list(args)
		reason = ""
		reason2 = ""
		for _num, _arg in enumerate(args):
			if _arg.startswith("-r"):
				for _reason_arg in args[_num + 1:]:
					if _reason_arg.startswith("-"):
						break
					else:
						reason += _reason_arg + " "
			if _arg.startswith("-h"):
				for _reason2_arg in args[_num + 1:]:
					if _reason2_arg.startswith("-"):
						break
					else:
						reason2 += _reason2_arg + " "
						
		await msg.edit(f'Grund: {reason}/nH')


def setup(bot):
	bot.add_cog(moderation(bot))
