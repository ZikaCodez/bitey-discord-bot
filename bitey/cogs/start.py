import discord
from discord.ext import commands
from discord.app_commands import command as cmd

from core.user import User

import time

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="start", description="Start command")
    async def start(self, ctx):
        embed = discord.Embed(
            title="Welcome to Bitey!",
            description=f"{self.bot.toothy} I'm Toothy, your personal assistant. I'll help you create and manage your restaurant.\n\n## What are you naming your restaurant?",
            color=0x00ff00
        )
        await ctx.send(embed=embed)
        name = await self.bot.wait_for("message", check=lambda m: m.author == ctx.author)
        name = name.content
        
        msg = await ctx.send(f"Doing the paperwork for your restaurant, {name}...")
        time.sleep(1)
        await msg.edit(content="Placing foundations...")
        time.sleep(1)
        await msg.edit(content="Setting up the kitchen...")
        time.sleep(1)
        await msg.edit(content="Hiring staff...")
        time.sleep(1)
        await User().create_user(ctx.author.id, name)
        await msg.edit(content="Opening the doors...")
        time.sleep(1)
        await msg.edit(content=f"Welcome to {name}!")
        
        
async def setup(bot):
    await bot.add_cog(Start(bot))