from typing import Optional
from nextcord.ext import commands
import nextcord
import time
from loguru import logger
from .Assets.badgefinder import badgefinder
from ..Helper.checks import ids


class util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo", aliases=["user", "ui"])
    async def userinfo(self, ctx, member: Optional[nextcord.Member]):
        """Gets informtion for a specific user"""
        
        if member == None:
            member = ctx.author

        badges = badgefinder(member)

        embed = nextcord.Embed(title=f"{member.display_name}", colour=member.colour)
        embed.add_field(name="User-Information", value=f"Name: {member.name}#{member.discriminator}\nID: {member.id}\nBadges: {badges}", inline=False)
        await ctx.send(embed=embed, delete_after=8)

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.message.delete()
        start_time = time.time()
        msg = await ctx.send("...")
        end_time = time.time()
        websocket = round(self.bot.latency * 1000)
        api = round((end_time - start_time) * 1000)
        
        embed = nextcord.Embed(title="Z00NI's Latenz(Websocket & API)")
        embed.add_field(name="WEBSOCKET", value=f"> {websocket}ms")
        embed.add_field(name="API", value=f"> {api}ms")
        await msg.edit(content="", embed=embed, delete_after=8)


    @commands.command(name="vips")
    async def vips(self, ctx):
        """Shows all VIP IDs/Users"""
        await ctx.message.delete()
        embed = nextcord.Embed(title="Z00NI VIPs", colour=nextcord.Colour.gold())
        vips = ""
        for _id in ids.VIPs:
            vips += f"<@{_id}>\n"
        embed.add_field(name="VIP-Liste", value=vips)
        await ctx.send(embed=embed, delete_after=8)
            

def setup(bot):
    bot.add_cog(util(bot))