import asyncio

from MainBot import MainBot


@MainBot.add_send_func("sender")
async def sender(from_bot, author, s):
    print(f"[{from_bot}] {author}: {s}")


import discord_bot
import telegram_bot


async def main():
    asyncio.create_task(MainBot.initializing())

    await asyncio.sleep(5)
    while True:
        await asyncio.sleep(2 ** 20)
        #  TODO: create normal infinity loop


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Closing...")
        #  TODO: close asyncio session
