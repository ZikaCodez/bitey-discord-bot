import discord
from discord.ext import commands

from core.errors import *
from core.utility import send_log

class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        dev = self.bot.get_user(510736807999307786)

        should_raise = False

        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.MissingRequiredArgument):
            err = f"`{error.param.name}` is a required argument that is missing!"

        elif isinstance(error, commands.BadArgument):
            err = f"`{error.param}` is not a valid argument!"

        elif isinstance(error, commands.MissingPermissions):
            err = f"You need `{', '.join(error.missing_permissions)}` permission(s) to use this command!"

        elif isinstance(error, commands.MemberNotFound):
            err = f"I couldn't find member **{error.param}**!"

        elif isinstance(error, commands.UserNotFound):
            err = f"I couldn't find user **{error.param}**!"
            
        ## CUSTOM ERRORS
        
        elif isinstance(error, UserAlreadyExists):
            err = "You already have a restaurant!"

        else:
            err = f"An unknown error has occurred!\n```\n{error}\n```"
            send_log("ERROR", f"An unknown error occurred: {error}")
            should_raise = True

        embed = discord.Embed(color=discord.Color.red(), description=err)
        embed.set_footer(text=f"Contact {dev} if you think this is a mistake!")
        await ctx.send(embed=embed)
        if should_raise:
            raise error


async def setup(bot):
    await bot.add_cog(ErrorHandling(bot))
