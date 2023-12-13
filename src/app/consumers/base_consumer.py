from abc import ABC, abstractmethod

from fastapi import FastAPI


class StartUpConsumerMixin(ABC):
    @abstractmethod
    async def startup(self):
        """FastAPI startup event"""
        raise NotImplementedError

    def _register_startup_event(self, app: FastAPI):
        app.add_event_handler("startup", self.startup)

    def register_events(self, app: FastAPI):
        self._register_startup_event(app)
