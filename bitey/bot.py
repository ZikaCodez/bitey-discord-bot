import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from core.utility import send_log

# Load environment variables
load_dotenv()

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

bot.toothy = "<:toothy:1329004192651677759>"

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("------")

    # Sync slash commands globally
    send_log("PROCESS", "Syncing commands...")
    
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            # Load the command file as a Cog
            await bot.load_extension(f"commands.{filename[:-3]}")
            print(f"Loaded command: {filename[:-3]}")
            
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

    # Load commands from the "commands" folder
            
    print("------")
    send_log("SUCCESS", "Bot is ready")

# Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))