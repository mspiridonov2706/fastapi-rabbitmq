from fastapi import FastAPI
from rodi import Container


def init_container(app: FastAPI) -> None:
    di_container = Container()
    setattr(app.state, str(Container), di_container)
