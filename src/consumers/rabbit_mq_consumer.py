from typing import Awaitable, Callable

from aio_pika.abc import AbstractIncomingMessage, AbstractRobustConnection, ExchangeType

from src.consumers.base_consumer import ABCConsumer


class RabbitMQConsumer(ABCConsumer):
    def __init__(self, connection: AbstractRobustConnection, handler: Callable[[str], Awaitable[None]]):
        self._connection = connection
        self._handler = handler

    async def consume(self):
        channel = await self._connection.channel()
        logs_exchange = await channel.declare_exchange("test4", ExchangeType.DIRECT)
        queue = await channel.declare_queue()

        await queue.bind(logs_exchange, routing_key="test")
        await queue.consume(self._proccess_message, no_ack=False)

    async def _proccess_message(self, message: AbstractIncomingMessage | None) -> None:
        if not message:
            return None

        await self._handler(str(message.body))
        await message.ack()
