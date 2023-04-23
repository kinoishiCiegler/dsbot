import disnake
from disnake.ext import commands
import os


intents2 = disnake.Intents.all()
bot = commands.Bot(command_prefix = "!", intents=intents2, test_guilds=[1093153045946323006])

@bot.event
async def on_ready():
    print("Bot is ready !")


    
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
    
bot.run("MTA5OTA2NTU5MzYwMjI2NTE1MQ.GyDbJf.xNzRjnAl0YRlwtzyMG69x4yrqE3UdaElU0P8vs")