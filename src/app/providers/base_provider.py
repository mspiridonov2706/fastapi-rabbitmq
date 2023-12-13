from abc import ABC, abstractmethod

from fastapi import FastAPI


class StartUpProviderMixin(ABC):
    @abstractmethod
    async def startup(self):
        """FastAPI startup event"""
        raise NotImplementedError

    def _register_startup_event(self, app: FastAPI):
        app.add_event_handler("startup", self.startup)

    def register_events(self, app: FastAPI):
        self._register_startup_event(app)


class ShutDownProviderMixin(ABC):
    @abstractmethod
    async def shutdown(self):
        """FastAPI shutdown event"""
        raise NotImplementedError

    def _register_shutdown_event(self, app: FastAPI):
        app.add_event_handler("shutdown", self.shutdown)

    def register_events(self, app: FastAPI):
        self._register_shutdown_event(app)


class BaseProviderMixin(StartUpProviderMixin, ShutDownProviderMixin):
    def register_events(self, app: FastAPI):
        self._register_startup_event(app)
        self._register_shutdown_event(app)
