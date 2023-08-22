import asyncio

import discord_bot
from MainBot import MainBot


@MainBot.add_send_func("sender1")
async def sender1(s):
    print(f"s1: {s}")


@MainBot.add_send_func("sender2")
async def sender2(s):
    print(f"s2: {s}")


async def main():
    # for name_bot in MainBot.init_func:
    #     print("Initializing {name_bot} bot")
    #     asyncio.create_task(MainBot.init_func[name_bot]())

    asyncio.create_task(MainBot.initializing())

    await asyncio.sleep(5)

    # await MainBot.send("sender1", "Hello World!")

    while True:
        await asyncio.sleep(2**20)
        #  TODO: create normal infinity loop


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Closing...")
        #  TODO: close asyncio session

