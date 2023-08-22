import asyncio


class MainBot:
    send_func = dict()
    init_func = dict()

    @classmethod
    def add_send_func(cls, bot_name):
        def wrapper(send_func):
            cls.send_func.update({bot_name: send_func})
            return send_func

        return wrapper

    @classmethod
    def add_init_func(cls, bot_name):
        def wrapper(init_func):
            cls.init_func.update({bot_name: init_func})
            return init_func

        return wrapper

    @classmethod
    async def initializing(cls):
        for name_bot in cls.init_func:
            print(f"Initializing {name_bot} bot")
            asyncio.create_task(MainBot.init_func[name_bot]())

    @classmethod
    async def send(cls, bot_name, content="", attachments: list = None):
        if attachments is None:
            attachments = []
        if content is None and attachments is None:
            raise "content and attachments is None"  # TODO: add Exception

        for filtered_name_bot in filter(lambda x: True if x != bot_name else False, MainBot.send_func):
            await MainBot.send_func[filtered_name_bot](content)
            #  TODO: add attachments

