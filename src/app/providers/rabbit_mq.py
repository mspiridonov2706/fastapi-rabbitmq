import logging

import aio_pika
from aio_pika.abc import AbstractRobustConnection
from rodi import Container

from src.app.providers.base_provider import BaseProviderMixin
from src.app.settings.rabbit_mq import RabbitMQSettings


logger = logging.getLogger().getChild("rabbitmq-provider")


class RabbitMQProvider(BaseProviderMixin):
    def __init__(self, container: Container, settings: RabbitMQSettings) -> None:
        self.di_container = container
        self.settings = settings

    async def startup(self):
        self.connection = await aio_pika.connect_robust(self.settings.dsn)
        logger.info("Connection has been established: %s", self.settings.dsn)
        self.di_container.register(AbstractRobustConnection, instance=self.connection)
        logger.info("Connection has been added into DI Container.")

    async def shutdown(self):
        if self.connection:
            await self.connection.close()
            logger.info("Connection has been closed.")
