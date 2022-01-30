import nextcord
from nextcord.ext.commands import Context
import asyncio

CANCEL = "<:statuscancelled:877295924903313408>"
BLOCKED = "<:statusblocked:877295924580352050>"
ONGOING = "<:statusongoing:877295924286742559>"
DONE = "<:statusdone:877295924592934922>"


async def load(self, ctx: Context, command: str):
    embed = nextcord.Embed(
        title=":gear: | Commander",
        description=
        f"Typ: **LOAD**\nDatei: **{command.upper()}**\n\nStatus: **LOADING** {ONGOING}",colour=nextcord.Colour.orange()
    )
    msg = await ctx.send(embed=embed)
    try:
        print(f"{command.upper()} is being loaded (MANUAL)")
        self.load_extension(f'src.cogs.{command}')
    except Exception as e:
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **LOAD**\nDatei: **{command.upper()}**\n\nStatus: **BLOCKED** {BLOCKED}",colour=nextcord.Colour.red()
        )
        await msg.edit(embed=embed)
        print(
            f"WARN: {command.upper()} has encountered an Error and has not been loaded (MANUAL)\n{e}"
        )
        return False
    else:
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **LOAD**\nDatei: **{command.upper()}**\n\nStatus: **DONE** {DONE}",colour=nextcord.Colour.green()
        )
        await msg.edit(embed=embed)
        print(f"INFO: {command.upper()} has been loaded (MANUAL)")
        return True


async def unload(self, ctx: Context, command: str):

    embed = nextcord.Embed(
        title=":gear: | Commander",
        description=
        f"Typ: **UNLOAD**\nDatei: **{command.upper()}**\n\nStatus: **LOADING** {ONGOING}",colour=nextcord.Colour.orange())

    msg = await ctx.send(embed=embed)

    try:

        print(f"INFO: {command.upper()} is being unloaded (MANUAL)")
        self.unload_extension(f'src.cogs.{command}')

    except Exception as e:

        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **UNLOAD**\nDatei: **{command.upper()}**\n\nStatus: **BLOCKED** {BLOCKED}",colour=nextcord.Colour.red()
        )

        await msg.edit(embed=embed)

        print(
            f"WARN: {command.upper()} has encountered an Error and has not been unloaded (MANUAL)\n{e}"
        )
        return False
    else:

        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **UNLOAD**\nDatei: **{command.upper()}**\n\nStatus: **DONE** {DONE}",colour=nextcord.Colour.green()
        )

        await msg.edit(embed=embed)

        print(f"INFO: {command.upper()} has been unloaded (MANUAL)")
        return True


async def reload(self, ctx: Context, command: str):
    embed = nextcord.Embed(
        title=":gear: | Commander",
        description=
        f"Typ: **RELOAD**\nDatei: **{command.upper()}**\n\nStatus: **LOADING** {ONGOING}",colour=nextcord.Colour.orange()
    )
    msg = await ctx.send(embed=embed)
    try:
        print(f"INFO: {command.upper()} is being reloaded (MANUAL)")
        self.unload_extension(f'src.cogs.{command}')
        await asyncio.sleep(1)
        self.load_extension(f'src.cogs.{command}')
    except Exception as e:
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **RELOAD**\nDatei: **{command.upper()}**\n\nStatus: **BLOCKED** {BLOCKED}",colour=nextcord.Colour.red()
        )
        await msg.edit(embed=embed)
        print(
            f"WARN: {command.upper()} has encountered an Error and has not been reloaded (MANUAL)\n{e}"
        )
        return False
    else:
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **RELOAD**\nDatei: **{command.upper()}**\n\nStatus: **DONE** {DONE}",colour=nextcord.Colour.green()
        )
        await msg.edit(embed=embed)
        print(f"INFO: {command.upper()} has been reloaded (MANUAL)")
        return True
