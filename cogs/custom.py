import random

import discord

from discord.ext import commands

from utils.classes import KurisuBot
from utils import lists

class Custom(commands.Cog):
    """A collection of commands mainly wrote by Jay"""
    def __init__(self, bot: KurisuBot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    async def megumin(self, ctx: commands.Context):
        """Jays Waifu"""
        async with self.bot.session.get("https://api.waifu.pics/sfw/megumin") as resp:
            await ctx.send(embed=discord.Embed(color=self.bot.ok_color).set_image(url=(await resp.json())["url"]))

    @commands.command()
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    async def shinobu(self, ctx: commands.Context):
        "Not Tadakuro. Blonde hair vamp girl from Monogatari"
        async with self.bot.session.get("https://api.waifu.pics/sfw/shinobu") as resp:
            await ctx.send(embed=discord.Embed(color=self.bot.ok_color).set_image(url=(await resp.json())["url"]))

    @commands.command()
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    async def mirai(self, ctx: commands.Context):
        """Keegs custom"""
        await ctx.send(random.choice(lists.mirai))

    @commands.command()
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    async def femboy(self, ctx: commands.Context):
        """Another one of Jay's customs"""
        await ctx.send(random.choice(lists.femboys))

    @commands.command()
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    async def trap(self, ctx: commands.Context):
        """Another custom command by Jay"""
        await ctx.send(random.choice(lists.traps))
    

    @commands.command()
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    async def boost(self, ctx: commands.Context):
        """Yet another custom"""
        await ctx.send("https://media1.tenor.com/images/68b7eca6ad0720a64a7e14d6bca83942/tenor.gif?itemid=11979611")

def setup(bot):
    bot.add_cog(Custom(bot))