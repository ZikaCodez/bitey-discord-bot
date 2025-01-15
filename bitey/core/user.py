from database import USERS
from errors import *
import datetime

class User:
    
    async def get_user(self, user_id:int): # Returns the USER data from the database IF FOUND
        data = await USERS.find_one({"_id": str(user_id)})
        return data
    
    async def check_user_exist(self, user_id): # Raises an error IF user NOT FOUND, otherwise, returns the USER
        user = await self.get_user(user_id)
        if not user:
            raise UserNotFound() # Raise error if user not found
        else:
            return user
    
    async def create_user(self, user_id, restaurant_name): # Creates a new USER in the database
        user_exist = await self.get_user(user_id)
        if user_exist:
            raise UserAlreadyExists(user_exist)
        
        # Initializing data
        data = {
            "_id": str(user_id),
            "bites": 30,
            "level": 1,
            "xp": 0,
            "challenges": [],
            "restaurant": {
                "name": restaurant_name,
                "menu": [],
                "kitchenLevel": 1,
                "kitchenXP": 0
            },
            "inventory": {
                "ingredients": [],
                "storageLimit": 50,
                "boosters": 0
            },
            "toothy": {
                "mood": 0,
                "lastFed": None,
                "notifications": [
                    {
                        "message": "<:toothy:1329004192651677759> Welcome to Bitey! I'm Toothy, your personal assistant. I'll help you manage your restaurant and keep you updated on challenges.",
                        "receivedAt": round(datetime.now().timestamp()),
                        "system": True,
                        "from": None,
                        "image": None
                    }
                ]
            }
        }
        
        USERS.insert_one(data)
        
    async def update_user(self, user_id, data):
        user = await self.check_user_exist()
        user = data
        await USERS.update_one({"_id": str(user._id)}, {"$set": {data}})