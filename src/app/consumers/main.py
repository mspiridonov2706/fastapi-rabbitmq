import logging

from fastapi import FastAPI
from rodi import Container

from src.app.consumers.rabbit_mq import RabbitMQStartupConsumer


logger = logging.getLogger().getChild("init-providers")


def init_consumers(app: FastAPI):
    di_container: Container = getattr(app.state, str(Container))

    rabbit_mq_test_consumer = RabbitMQStartupConsumer(di_container=di_container)
    rabbit_mq_test_consumer.register_events(app=app)

    logger.info("RabbitMQTestConsumer has been inited")
