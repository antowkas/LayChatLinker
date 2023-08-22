import asyncio

import discord
from discord import default_permissions
from discord.ext import commands
from config import discord as cfg
from MainBot import MainBot

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=cfg.PREFIX, intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.slash_command(name='get_channel_id', description='get channel id')
@default_permissions(administrator=True)
async def __get_channel_id(ctx):
    await ctx.respond(f"Channel id: `{ctx.channel.id}`")


@bot.event
async def on_message(message):
    if message.channel.id != cfg.CHANNEL or message.author.bot:
        return

    msg = ""
    if message.content:
        msg += message.content
    if message.attachments:  # TODO: normal files not urls
        msg += '\n' + '\n'.join(map(lambda x: x.url, message.attachments))
    if not msg:
        return

    await MainBot.send(cfg.BOT_NAME, msg)
    # await send_message(msg)


def get_channel():
    return bot.get_channel(cfg.CHANNEL)


@MainBot.add_send_func(cfg.BOT_NAME)
async def send_message(message):  # TODO: add attachments
    channel = get_channel()
    await channel.send(message)


@MainBot.add_init_func(cfg.BOT_NAME)
async def initialization():
    asyncio.create_task(bot.start(cfg.TOKEN))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(initialization())

