import asyncio

from sys import path
import types
from os import listdir
from os.path import isfile, join
import discord
from discord.ext import commands
import CONFIG

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="☺", intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready!")


if __name__ == '__main__':
    path.insert(1, CONFIG.MODULES_PATH)
    for file_name in [f for f in listdir(CONFIG.MODULES_PATH)
                      if isfile(join(CONFIG.MODULES_PATH, f)) and f.endswith(".py")]:
        module = __import__(file_name[:-3])

        if "bot_init" in [getattr(module, a).__name__ for a in dir(module)
                          if isinstance(getattr(module, a), types.FunctionType)]:
            print(f"Initializing {file_name}")
            module.bot_init(bot)
    bot.run(CONFIG.TOKEN)
