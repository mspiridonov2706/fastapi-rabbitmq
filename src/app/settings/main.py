from fastapi import FastAPI
from rodi import Container

from src.app.settings.project import ProjectSettings
from src.app.settings.rabbit_mq import RabbitMQSettings


class ApplicationSettings:
    project = ProjectSettings()
    rabbit_mq = RabbitMQSettings()


def init_settings(app: FastAPI) -> None:
    di_container: Container = getattr(app.state, str(Container))
    settings = ApplicationSettings()
    di_container.register(ApplicationSettings, instance=settings)
