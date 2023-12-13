from fastapi import FastAPI

from src.app.consumers import init_consumers
from src.app.dependencies import init_container
from src.app.logger import init_logger
from src.app.providers import init_providers
from src.app.settings import init_settings


def create_app() -> FastAPI:
    app = FastAPI()
    init_container(app)
    init_settings(app)
    init_logger(app)
    init_providers(app)
    init_consumers(app)

    return app


app = create_app()
