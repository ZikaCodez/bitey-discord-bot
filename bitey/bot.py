import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("------")

    # Sync slash commands globally
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

    # Load commands from the "commands" folder
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            # Load the command file as a Cog
            await bot.load_extension(f"commands.{filename[:-3]}")
            print(f"Loaded command: {filename[:-3]}")

# Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))