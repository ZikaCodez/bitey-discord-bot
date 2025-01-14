# **Bitey - The Food-Themed Discord Bot** 🦈🍔

**Bitey** is a fun and interactive Discord bot centered around food, restaurants, and friendly competition. Grow your virtual restaurant, serve delicious dishes, and compete in cooking challenges with friends—all while enjoying the company of **Toothy**, our friendly shark mascot! 

Whether you're a foodie or just looking for a fun bot to spice up your server, Bitey is here to serve up smiles and good vibes. 🎉

---

## **Features** 🎮
- 🍔 **Virtual Restaurant Management**: Create and grow your own restaurant or food truck.
- 🎯 **Cooking Challenges**: Compete in timed challenges to create the best dishes.
- 🦈 **Toothy the Mascot**: Interact with our friendly shark mascot for fun and rewards.
- 🎉 **Events and Collaborations**: Host food festivals and team up with friends.
- 🛠️ **Customizable Menus**: Create unique dishes and unlock rare recipes.
- 📊 **Leaderboards**: Track your progress and compete for the top spot.

---

## **Installation** ⚙️

### **Prerequisites**
- Python 3.8 or higher
- A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications)
- MongoDB (or a MongoDB Atlas cluster) for database storage

### **Steps**
1. Clone the repository:
  ```bash
   git clone https://github.com/ZikaCodez/bitey-discord-bot.git
   cd bitey-discord-bot
   ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Create a `.env` file in the root directory and add your bot token and MongoDB URI:
  ```env
  DISCORD_TOKEN=your-bot-token-here
  MONGODB_URI=your-mongodb-uri-here
  ```
4. Start the bot
  ```bash
  python bot.py
  ```

---

### **Essential Slash Commands** 🎮

1. **Restaurant Management** 🍽️
   - `/open` - Open your restaurant or food truck for the day.
   - `/upgrade` - Upgrade your kitchen, dining area, or food truck.
   - `/decorate` - Customize your restaurant’s theme or decor.

2. **Cooking and Serving** 👨‍🍳
   - `/cook [recipe]` - Cook a dish from your menu.
   - `/serve [dish]` - Serve a dish to a customer.
   - `/rush` - Handle a rush of customers for bonus rewards.

3. **Challenges and Events** 🎉
   - `/challenge [difficulty]` - Start a cooking challenge (easy, medium, hard).
   - `/event` - Host a special event like a food festival or pop-up shop.
   - `/leaderboard` - Check the server-wide leaderboard for top chefs.

4. **Toothy the Mascot** 🦈
   - `/toothy feed` - Feed Toothy and earn rewards.
   - `/toothy play` - Play a mini-game with Toothy for bonus coins.

5. **Economy and Trading** 💰
   - `/balance` - Check your coins and earnings.
   - `/buy [item]` - Purchase ingredients, decor, or upgrades.
   - `/trade [@user]` - Trade items or coins with another player.

6. **Help and Info** ❓
   - `/help` - Get a list of all available commands.
   - `/tutorial` - Start a tutorial to learn how to play.

### **Example Usage**:
- `/open` - Opens your restaurant for the day.
- `/cook pizza` - Cooks a pizza from your menu.
- `/challenge hard` - Starts a hard cooking challenge.
- `/toothy feed` - Feeds Toothy and earns rewards.

---

## **Contributing** 🤝

We welcome contributions! Here’s how you can help:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
  ```bash
  git checkout -b feature/your-feature-name
  ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request and describe your changes.

Please follow the [contribution guidelines](CONTRIBUTING.md) for more details.

---

## **License** 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Support** 💬

If you have any questions, issues, or suggestions, feel free to:
- Open an issue on GitHub.
- Join our [Discord server](https://discord.gg/F9u4QRYKQQ) for support.

---

**Let’s make Bitey the most delicious bot on Discord!** 🦈🍕
