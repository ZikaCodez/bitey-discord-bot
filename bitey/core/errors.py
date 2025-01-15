import discord
from discord.ext import commands

class Error(commands.CommandError):
    pass

class UserAlreadyExists(Error): # Attempt of creating a USER that already exists
    def __init__(self, data):
        self.data = data

    pass

class UserNotFound(Error): # No data was found for USER
    pass

class RestaurantNameTaken(Error):
    def __init__(self, name):
        self.name = name
    
    pass