from datetime import datetime
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import  Context
from nextcord import Embed, Colour
from loguru import logger

from source.Bot.bot import stop

from .Assets.dev import load, unload, reload
from ..Helper.checks import is_staff

class developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name="on_ready")
    async def on_ready(self):
        logger.log("BOT", f"Logged in as: {self.bot.user}")
        logger.log("BOT", f"Commands need to be loaded manually(ofc developer is loaded ^^)")

    @commands.command(name="shutdownbot", aliases=["stopbot", "botstop", "shutdown", "stop"])
    @is_staff()
    async def shutdownbot(self, ctx):
        await stop(ctx)

    @commands.command(name="load", aliases=["enable", "l"])
    @is_staff()
    async def load(self, ctx: Context, module: str):
        """Loads a Cog"""
        embed = Embed(title="Load | Loading...", colour=Colour.orange(), timestamp=ctx.message.created_at)
        msg = await ctx.send(embed=embed)
        state = await load(self, module)
        if state == True:
            embed = Embed(title="Load | Success", colour=Colour.brand_red(), timestamp=ctx.message.created_at)
            await msg.edit(embed=embed, delete_after=4)
        elif state == False:
            embed = Embed(title="Load | Failure", description="Siehe Konsole für mehr Informationen.", colour=Colour.brand_red(), timestamp=ctx.message.created_at)
            await msg.edit(embed=embed, delete_after=4)

    @commands.command(name="unload", aliases=["disable", "unl"])
    @is_staff()
    async def unload(self, ctx: Context, module: str):
        """Unloads a Cog"""
        embed = Embed(title="Unload | Loading...", colour=Colour.orange(), timestamp=ctx.message.created_at)
        msg = await ctx.send(embed=embed)
        state = await unload(self, module)
        if state == True:
            embed = Embed(title="Unload | Success", colour=Colour.brand_red(), timestamp=ctx.message.created_at)
            await msg.edit(embed=embed, delete_after=4)
        elif state == False:
            embed = Embed(title="Unload | Failure", description="Siehe Konsole für mehr Informationen.", colour=Colour.brand_red(), timestamp=ctx.message.created_at)
            await msg.edit(embed=embed, delete_after=4)

    @commands.command(name="reload", aliases=["r"])
    @is_staff()
    async def reload(self, ctx: Context, module: str):
        """Reloads a Cog"""
        embed = Embed(title="Reload | Loading...", colour=Colour.orange(), timestamp=ctx.message.created_at)
        msg = await ctx.send(embed=embed)
        state = await reload(self, module)
        if state == True:
            embed = Embed(title="Reload | Success", colour=Colour.brand_red(), timestamp=ctx.message.created_at)
            await msg.edit(embed=embed, delete_after=4)
        elif state == False:
            embed = Embed(title="Reload | Failure", description="Siehe Konsole für mehr Informationen.", colour=Colour.brand_red(), timestamp=ctx.message.created_at)
            await msg.edit(embed=embed, delete_after=4)

    async def cog_command_error(self, ctx, e):

        usage = "`load/unload/reload <Modul>`"
        perms = "`STAFF`"


        embed = Embed(title="Developer | Failure", colour=Colour.brand_red(), timestamp=ctx.message.created_at)

        if isinstance(e, commands.CommandError):
            embed.add_field(name=":warning: Fehler", value=f"Errorcode:\n> {e}", inline=False)
            embed.set_footer(text="Selbstzerstörung der Nachricht in 8 Sekunden")

        if isinstance(e, commands.MissingRequiredArgument):
            embed.add_field(name=":page_facing_up: Fehlerhafte Nutzung:", value=f"\n> {usage}", inline=False)
            return await ctx.send(embed=embed, delete_after=8)

        if isinstance(e, commands.CheckFailure):
            embed.add_field(name=":lock: Fehlende Rechte:", value=f"Benötigte Rechte:\n> {perms}", inline=False)
            return await ctx.send(embed=embed, delete_after=8)    

def setup(bot):
    bot.add_cog(developer(bot))