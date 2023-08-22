import discord
from discord.ext import commands
from config import discord as cfg

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=cfg.PREFIX, intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready!")


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

    print(message.channel.id)

    # TODO: send "main.py" (Main.send(from="DISCORD", content="", attachments=[]))
    await send_message(msg)


def get_channel():
    return bot.get_channel(cfg.CHANNEL)


async def send_message(message):  # TODO: add attachments
    channel = get_channel()
    await channel.send(message)


if __name__ == '__main__':
    bot.run(cfg.TOKEN)
