from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))

# Database
MAIN_DB = client.MainDB

# Collections
USERS = MAIN_DB.users               # users collection
ITEMS = MAIN_DB.items               # items collection (menu items)
BOOSTERS = MAIN_DB.boosters         # boosters collection
INGREDIENTS = MAIN_DB.ingredients   # cooking ingredients
CHALLENGES = MAIN_DB.challenges     # daily challenges
