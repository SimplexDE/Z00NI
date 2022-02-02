import nextcord
import os

version = os.getenv("version")

async def bot_presence(self):
    await self.change_presence(
        activity=nextcord.Activity(
            type=nextcord.ActivityType.watching,
            name=f"!help | {version}"),
            status=nextcord.Status.online)
