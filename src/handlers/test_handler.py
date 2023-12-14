from src.handlers.base_handler import ABCMessageHandler


class TestHandler(ABCMessageHandler):
    async def __call__(self, message: str):
        print(message)
