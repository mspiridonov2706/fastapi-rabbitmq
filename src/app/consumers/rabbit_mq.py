import asyncio
import logging

from aio_pika.abc import AbstractRobustConnection
from rodi import Container

from src.app.consumers.base_consumer import StartUpConsumerMixin
from src.consumers.rabbit_mq_consumer import RabbitMQConsumer
from src.handlers.test_handler import TestHandler


logger = logging.getLogger().getChild("consumer")


class RabbitMQStartupConsumer(StartUpConsumerMixin):
    def __init__(self, di_container: Container) -> None:
        self.di_container = di_container

    async def startup(self):
        connection = self.di_container.resolve(AbstractRobustConnection)
        handler = TestHandler()
        consumer = RabbitMQConsumer(connection=connection, handler=handler)
        await asyncio.create_task(consumer.consume())
        logger.info("Consumer %s has been created", self)
