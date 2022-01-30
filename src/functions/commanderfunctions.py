import nextcord
from nextcord.ext.commands import Context
import asyncio
from loguru import logger

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
        logger.info(f"{command.upper()} wird geladen.")
        self.load_extension(f'src.cogs.{command}')
    except Exception as e:
        logger.error(f"{command.upper()} wurde nicht geladen aufgrund von einem Fehler.")
        logger.error(e)
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **LOAD**\nDatei: **{command.upper()}**\n\nStatus: **BLOCKED** {BLOCKED}",colour=nextcord.Colour.red()
        )
        await msg.edit(embed=embed)
        return False
    else:
        logger.success(f"{command.upper()} geladen.")
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **LOAD**\nDatei: **{command.upper()}**\n\nStatus: **DONE** {DONE}",colour=nextcord.Colour.green()
        )
        await msg.edit(embed=embed)
        return True


async def unload(self, ctx: Context, command: str):
    embed = nextcord.Embed(
        title=":gear: | Commander",
        description=
        f"Typ: **UNLOAD**\nDatei: **{command.upper()}**\n\nStatus: **LOADING** {ONGOING}",colour=nextcord.Colour.orange())

    msg = await ctx.send(embed=embed)

    try:
        logger.info(f"{command.upper()} wird entladen.")
        self.unload_extension(f'src.cogs.{command}')

    except Exception as e:
        logger.error(f"{command.upper()} wurde nicht entladen aufgrund eines Fehlers.")
        logger.error(e)
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **UNLOAD**\nDatei: **{command.upper()}**\n\nStatus: **BLOCKED** {BLOCKED}",colour=nextcord.Colour.red()
        )

        await msg.edit(embed=embed)
        return False
    else:
        logger.success(f"{command.upper()} entladen.")
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **UNLOAD**\nDatei: **{command.upper()}**\n\nStatus: **DONE** {DONE}",colour=nextcord.Colour.green()
        )

        await msg.edit(embed=embed)

        return True


async def reload(self, ctx: Context, command: str):
    embed = nextcord.Embed(
        title=":gear: | Commander",
        description=
        f"Typ: **RELOAD**\nDatei: **{command.upper()}**\n\nStatus: **LOADING** {ONGOING}",colour=nextcord.Colour.orange()
    )
    msg = await ctx.send(embed=embed)
    try:
        logger.info(f"{command.upper()} wird neugeladen")
        print(f"INFO: {command.upper()} is being reloaded (MANUAL)")
        self.unload_extension(f'src.cogs.{command}')
        await asyncio.sleep(1)
        self.load_extension(f'src.cogs.{command}')
    except Exception as e:
        logger.error(f"{command.upper()} wurde aufgrund eines Fehlers nicht neugeladen.")
        logger.error(e)
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **RELOAD**\nDatei: **{command.upper()}**\n\nStatus: **BLOCKED** {BLOCKED}",colour=nextcord.Colour.red()
        )
        await msg.edit(embed=embed)
        return False
    else:
        logger.success(f"{command.upper()} neugeladen")
        embed = nextcord.Embed(
            title=":gear: | Commander",
            description=
            f"Typ: **RELOAD**\nDatei: **{command.upper()}**\n\nStatus: **DONE** {DONE}",colour=nextcord.Colour.green()
        )
        await msg.edit(embed=embed)
        return True
