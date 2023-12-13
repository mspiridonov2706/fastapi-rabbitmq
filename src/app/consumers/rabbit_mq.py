import abc
import asyncio
import logging

from aio_pika.abc import AbstractIncomingMessage, AbstractRobustConnection, ExchangeType
from rodi import Container

from src.app.consumers.base_consumer import StartUpConsumerMixin


logger = logging.getLogger().getChild("consumer")


class ABCMessageHandler(abc.ABC):
    @abc.abstractmethod
    async def __call__(self, message: str):
        raise NotImplementedError


class TestHandler(ABCMessageHandler):
    async def __call__(self, message: str):
        print(message)


class RabbitMQTestConsumer(StartUpConsumerMixin):
    def __init__(
        self,
        di_container: Container,
        handler: ABCMessageHandler,
        connection: AbstractRobustConnection | None = None,
    ) -> None:
        self.di_container = di_container
        self.message_handler = handler
        self.connection = connection

    async def startup(self):
        self.connection = self.di_container.resolve(AbstractRobustConnection)
        await asyncio.create_task(self._consume())
        logger.info("Consumer %s has been created", self)

    async def _consume(self) -> None:
        if not self.connection:
            return None

        channel = await self.connection.channel()
        logs_exchange = await channel.declare_exchange("test3", ExchangeType.FANOUT)
        queue = await channel.declare_queue()

        await queue.bind(logs_exchange)
        await queue.consume(self._proccess_message, no_ack=False)

    async def _proccess_message(self, message: AbstractIncomingMessage | None) -> None:
        if not message:
            return None

        await self.message_handler(str(message.body))
        await message.ack()
