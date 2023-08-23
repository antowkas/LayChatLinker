import asyncio

from pprint import pprint

from aiogram import Bot, Dispatcher, types
from aiogram.client.session.middlewares.request_logging import RequestLogging
from aiogram.filters.command import Command
from aiogram.methods import GetUpdates

from MainBot import MainBot
from config import telegram as cfg

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher()


@dp.message(Command("get_chat_id"))
async def cmd_start(message: types.Message):
    await message.reply(f"Chat id: {message.chat.id}")


@dp.message()
async def on_message(message: types.Message):
    if message.chat.id != cfg.CHANNEL or message.from_user.is_bot:
        return

    # for photoSize in message.photo:
    #     pprint(photoSize)
    #     pprint(await bot.get_file(photoSize.file_id))
    #     return

    msg = ""
    if message.text:
        msg += message.text
    if message.caption:
        msg += message.caption
    if message.photo:  # TODO: normal files
        # print(message)
        msg += '\n[Photo (WIP)]'
    if message.audio:
        msg += '\n[Audio (WIP)]'
    if message.document:
        msg += '\n[Doc (WIP)]'
    if message.voice:
        msg += '\n[Voice (WIP)]'
    if message.video:
        msg += '\n[Video (WIP)]'
    if not msg:
        return

    await MainBot.send(cfg.BOT_NAME, message.from_user.full_name, msg)
    # await send_message(f"{message.from_user.full_name}: {message.text}")


def get_channel():
    return cfg.CHANNEL


@MainBot.add_send_func(cfg.BOT_NAME)
async def send_message(from_bot, from_name, message):  # TODO: add attachments
    channel = get_channel()
    message = f"\\[{from_bot}] {from_name}: {message}"
    await bot.send_message(channel, message, parse_mode="Markdown")


@MainBot.add_init_func(cfg.BOT_NAME)
async def initialization():
    asyncio.create_task(dp.start_polling(bot))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(initialization())
