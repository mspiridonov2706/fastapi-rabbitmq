import logging

from fastapi import FastAPI
from rodi import Container

from src.app.providers.rabbit_mq import RabbitMQProvider
from src.app.settings import ApplicationSettings


logger = logging.getLogger().getChild("init-providers")


def init_providers(app: FastAPI):
    di_container: Container = getattr(app.state, str(Container))
    settings = di_container.resolve(ApplicationSettings)

    rabbit_mq_provider = RabbitMQProvider(container=di_container, settings=settings.rabbit_mq)
    rabbit_mq_provider.register_events(app=app)

    logger.info("RabbitMQ Provider has been inited: %s", settings.rabbit_mq)
