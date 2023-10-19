from typing import Literal
import tomllib

from discord.ext import commands
import discord

from .kurisu import KurisuBot, ConfigHandler

config = ConfigHandler()

class KurisuContext(commands.Context):
    """Custom Context"""

    bot: KurisuBot

    async def send_ok(self, content: str):
        await self.send(
            embed=discord.Embed(
                description=content, color=config.get("ok_color", "Core")
            )
        )

    async def send_info(self, content: str):
        await self.send(
            embed=discord.Embed(description=content, color=config.get("info_color", "Core"))
        )

    async def send_error(self, content: str):
        await self.send(
            embed=discord.Embed(
                description=content, color=config.get("error_color", "Core")
            )
        )
