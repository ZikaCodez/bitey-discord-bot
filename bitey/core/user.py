from .database import USERS
from .errors import *
import datetime
from .utility import *

class User:
    
    async def get_user(self, user_id:int):
        # Gets user data from the database by user_id
        # Returns None if not found
        # Parameters:
        #   user_id (int): The ID of the user to look up
        # Returns:
        #   dict: User data if found, None otherwise
        data = USERS.find_one({"_id": str(user_id)})
        return data
    
    async def find_restaurant(self, restaurant_name):
        # Finds a user by their restaurant name
        # Parameters: 
        #   restaurant_name (str): Name of the restaurant to search for
        # Returns:
        #   dict: User data if found, None otherwise
        data = USERS.find_one({"restaurant.name": restaurant_name})
        return data
    
    async def check_user_exist(self, user_id):
        # Checks if a user exists in the database
        # Parameters:
        #   user_id (int): The ID of the user to check
        # Returns:
        #   dict: User data if found
        # Raises:
        #   UserNotFound: If user does not exist
        user = await self.get_user(user_id)
        if not user:
            raise UserNotFound()
        else:
            return user
    
    async def create_user(self, user_id, restaurant_name):
        # Creates a new user in the database with initial game data
        # Parameters:
        #   user_id (int): The ID of the new user
        #   restaurant_name (str): Name for the user's restaurant
        # Raises:
        #   UserAlreadyExists: If user_id is already registered
        #   RestaurantNameTaken: If restaurant_name is already in use
        send_log("PROCESS", f"Creating a new user with ID {user_id} and restaurant name '{restaurant_name}'")
        
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
            "_id": str(user_id),  # Unique identifier for the user
            "bites": 30,  # In-game currency
            "level": 1,  # Player level
            "xp": 0,  # Experience points
            "challenges": [],  # List of active/completed challenges
            "restaurant": {
                "name": restaurant_name,  # User's restaurant name
                "menu": [],  # List of dishes available in the restaurant
                "kitchenLevel": 1,  # The higher the kitchen level, the faster the cooking process
            },
            "inventory": {
                "ingredients": [],  # List of ingredients owned by user
                "storageLimit": 50,  # Maximum number of ingredients that can be stored
                "boosters": []  # Array of IDs of collected boosters
            },
            "toothy": {
                "mood": 0,  # 0 = neutral, 1 = happy, 2 = hungry
                "lastFed": None,  # Timestamp of when Toothy was last fed
                "notifications": [
                    {
                        "message": "<:toothy:1329004192651677759> Welcome to Bitey! I'm Toothy, your personal assistant. I'll help you manage your restaurant and keep you updated on challenges.",
                        "receivedAt": round(datetime.datetime.now().timestamp()),  # When notification was created
                        "system": True,  # Whether this is a system notification
                        "from": None,  # Source of notification if not system
                        "image": None  # Optional image attachment
                    }
                ]
            }
        }
        
        user = USERS.insert_one(data)
        print(user)
        
        send_log("SUCCESS", f"User with ID {user_id} and restaurant name {restaurant_name} has been created")
        
    async def update_user(self, user_id, data):
        # Updates user data in the database
        # Parameters:
        #   user_id (int): The ID of the user to update
        #   data (dict): The new data to update
        # Raises:
        #   UserNotFound: If user does not exist
        user = await self.check_user_exist()
        await USERS.update_one({"_id": str(user_id)}, {"$set": data})