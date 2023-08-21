import discord
from discord.ext import commands
from config import discord as cfg

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="☺", intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready!")


if __name__ == '__main__':
    bot.run(cfg.TOKEN)
