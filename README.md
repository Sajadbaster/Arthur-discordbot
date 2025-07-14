# Arthur Discord Bot
Arthur Bot is a multi-purpose Discord bot built with discord.py. It's designed to be a helpful and fun addition to any server.
This is my first major project, so there might be bugs or areas for improvement. All feedback is welcome!
✨ Features
 * Weather Forecasts: Get the current weather for any city.
 * Magic 8-Ball: Have a question? Get a mysterious answer from the bot.
 * Server Economy: A built-in currency and banking system for users.
 * Simple Games: Play classic games against the bot.
 * Moderation Tools: A suite of commands to help server moderators.
# 🚀 Installation & Setup
Follow these steps to get Arthur running on your own server.
1. Prerequisites
 * You must have Python 3.8 or newer installed.
 * You should be familiar with cloning a Git repository.
2. Clone the Repository
Open your terminal or command prompt and run the following command to download the files:
```
git clone https://github.com/sajadbaster/Arthur-discordbot
cd Arthur-discordbot
```


3. Install Dependencies
Install all the required Python libraries by running:
```
pip install -r requirements.txt
```

4. Configure Your Keys
The bot needs API keys to function.
 * Find the Api.template.json file in the project.
 * Make a copy of it and rename the copy to Api.json.
 * Open Api.json and fill in your unique keys:
   * discordTokenCode: Get this from the Discord Developer Portal.
   * weatherapi: Get this from the OpenWeatherMap website.
5. Run the Bot
You're all set! Start the bot with this command:
python Main.py

# 🤖 Commands
Here is a list of the primary commands available:
| Command | Description |
|---|---|
| /weather <city> | Shows the current weather conditions for the specified city. |
| /botofanswers <question> | Ask a question and receive a wise, or perhaps witty, answer. |
| /profile [user] | Displays your profile or the profile of a mentioned user, showing money and user ID. |
| /mba | Creates a new bank account for you in the bot's database. |
| /rps <play> | Play a game of Rock, Paper, Scissors against Arthur. Your play can be rock, paper, or scissors. |
| /give-money <amount> <user> | Feel generous? Give some of your in-bot money to another user. |
| /rdice [min] [max] | Rolls a magical die. You can specify a minimum and maximum number. Defaults to 1-6. |
| /mute <user> <time> [reason] | Mutes a user for a specified number of minutes. |
| /unmute <user> | Unmutes a previously muted user. |
| /kick <user> [reason] | Kicks a user from the server. |
| /ban <user> [reason] | Bans a user from the server. |
| /unban <user_id> | Unbans a user using their unique user ID. |
| /clear <amount> | Deletes a specified number of messages from the current channel. |
<br>