from database import USERS
from errors import *
import datetime
from utility import *

class User:
    
    async def get_user(self, user_id:int): # Returns the USER data from the database IF FOUND
        data = await USERS.find_one({"_id": str(user_id)})
        return data
    
    async def find_restaurant(self, restaurant_name):
        data = await USERS.find_one({"restaurant.name": restaurant_name})
        return data
    
    async def check_user_exist(self, user_id): # Raises an error IF user NOT FOUND, otherwise, returns the USER
        user = await self.get_user(user_id)
        if not user:
            raise UserNotFound() # Raise error if user not found
        else:
            return user
    
    async def create_user(self, user_id, restaurant_name): # Creates a new USER in the database
        send_log("PROCESS", f"Creating a new user with ID {user_id} and restaurant name {restaurant_name}")
        
        user_exist = await self.get_user(user_id)
        if user_exist:
            send_log("ERROR", f"User with ID {user_id} already exists")
            raise UserAlreadyExists(user_exist)
        
        restaurant_exist = await self.find_restaurant(restaurant_name)
        if restaurant_exist:
            send_log("ERROR", f"Restaurant name {restaurant_name} is already taken")
            raise RestaurantNameTaken(restaurant_name)
        
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
                "kitchenLevel": 1, # The higher the kitchen level, the faster the cooking process
                "kitchenXP": 0
            },
            "inventory": {
                "ingredients": [],
                "storageLimit": 50,
                "boosters": [] # Array of IDs of collected boosters
            },
            "toothy": {
                "mood": 0, # 0 = neutral, 1 = happy, 2 = hungry
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
        
        send_log("SUCCESS", f"User with ID {user_id} and restaurant name {restaurant_name} has been created")
        
    async def update_user(self, user_id, data):
        user = await self.check_user_exist()
        user = data
        await USERS.update_one({"_id": str(user._id)}, {"$set": {data}})