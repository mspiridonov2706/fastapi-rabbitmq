from logging import config as logging_config

from fastapi import FastAPI
from rodi import Container

from src.app.settings import ApplicationSettings
from src.app.settings.project import ProjectSettings


def init_logger(app: FastAPI) -> None:
    di_container: Container = getattr(app.state, str(Container))
    settings = di_container.resolve(ApplicationSettings)

    logging_config.dictConfig(get_logger_config(settings.project))


def get_logger_config(settings: ProjectSettings) -> dict:
    logger_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "level": settings.log_level,
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
        },
        "loggers": {
            "": {
                "handlers": ["console"],
                "level": settings.log_level,
            },
        },
    }
    return logger_config
