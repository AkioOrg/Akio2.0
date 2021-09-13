from copy import copy

import discord

from discord.ext import commands

from utils.classes import KurisuBot

class NoPrefix(commands.Cog):
    """No Command Prefix Cog. For Bot Owners"""
    def __init__(self, bot: KurisuBot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        gc = self.bot.get_config
        if message.author.id not in self.bot.owner_ids:
            return
        msg = copy(message)
        msg.content = f"{self.bot.prefixes.get(str(message.guild.id)) or gc('config', 'config', 'prefix')}{msg.content}"
        await self.bot.process_commands(msg)

def setup(bot):
    bot.add_cog(NoPrefix(bot))