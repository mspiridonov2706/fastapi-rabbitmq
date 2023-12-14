import abc


class ABCMessageHandler(abc.ABC):
    @abc.abstractmethod
    async def __call__(self, message: str):
        raise NotImplementedError
