from discord.ext import commands
import discord

from utils.classes import KurisuBot


class Help(commands.Cog):
    """Help related commands"""

    def __init__(self, bot: KurisuBot):
        self.bot = bot

    @commands.command(aliases=["cogs"])
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def modules(self, ctx: commands.Context):
        text = ""
        for _ in self.bot.cogs.keys():
            cog = self.bot.get_cog(_)
            if len(cog.get_commands()) != 0:
                text += f"\n{_}"
                mod_list = text.split("\n")
        await ctx.send(
            embed=discord.Embed(
                title="Available Modules",
                description="```apache\n" + "\n".join(sorted(mod_list)) + "\n```",
                color=self.bot.ok_color,
            )
        )

    @commands.group(invoke_without_command=True)
    async def help(self, ctx: commands.Context):
        """Shows information on a specific command or module"""
        await ctx.send(
            embed=discord.Embed(
                title=f"Hi I'm {self.bot.user.name}",
                description=f"{self.bot.user.name} is a multi-modular all purpose bot built with Discord.py",
                color=self.bot.ok_color,
            )
            .set_thumbnail(url=self.bot.user.avatar.url)
            .set_footer(
                icon_url=self.bot.user.avatar.url,
                text=f"{self.bot.user} has been serving users since {self.bot.user.created_at.strftime('%c')}",
            )
            .add_field(
                name="Modules",
                value=(
                    f"Run `{ctx.clean_prefix}modules` for a list of active modules\n\n"
                    f"Run `{ctx.clean_prefix}help module <modulename>` for info on a specific module"
                ),
            )
            .add_field(
                name="Commands",
                value=f"Run `{ctx.clean_prefix}help command <commandname>` for info on a command",
            )
        )

    @help.command(aliases=["cmd", "c"])
    async def command(self, ctx: commands.Context, *, target: str):
        cmd = self.bot.get_command(target.lower())
        if cmd:
            cmd_aliases = "\n".join(cmd.aliases)
            embed = discord.Embed(
                title=f"__{cmd.name}__",
                description=f"Description: {cmd.help}",
                color=self.bot.ok_color,
            )
            embed.add_field(
                name="Usage",
                value=f"`{ctx.clean_prefix}{cmd.name} {'' if not cmd.signature else cmd.signature}`",
            )
            embed.add_field(name="Module\Cog", value=f"`{cmd.cog_name}`")
            if cmd.aliases:
                embed.add_field(name="Aliases", value=f"```\n{cmd_aliases}\n```")
            if isinstance(cmd, commands.Group):
                group_commands = "\n".join(map(str, cmd.commands))
                embed.add_field(name="Group Commands", value=f"```\n{group_commands}\n```")
            return await ctx.send(embed=embed)
        else:
            return await ctx.send(
                embed=discord.Embed(description=f"COMMAND NOT FOUND", color=self.bot.error_color)
            )

    @help.command(aliases=["mod", "m"])
    async def module(self, ctx: commands.Context, target: str):
        found = []
        for c in self.bot.cogs:
            if str(c).lower().startswith(target.lower()):
                found.append(c)
            if c.lower() == target.lower():
                found = [c]
                break
        if found:
            cog = self.bot.get_cog(found[0])
            cog_commands = "\n".join(sorted(map(str, cog.get_commands()))) or None
            return await ctx.send(
                embed=discord.Embed(
                    title=cog.qualified_name or target,
                    color=self.bot.ok_color,
                )
                .add_field(name="Description", value=f"`{cog.description or None}`")
                .add_field(name="Commands", value=f"```\n{cog_commands}\n```")
                .set_footer(
                    text=f"Do {ctx.clean_prefix}help command <commandname> for help with a command"
                )
            )
        if not found:
            return await ctx.send(
                embed=discord.Embed(
                    description=f"**MODULE NOT FOUND**", color=self.bot.error_color
                )
            )


def setup(bot):
    bot.add_cog(Help(bot))
