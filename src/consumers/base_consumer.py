import abc


class ABCConsumer(abc.ABC):
    @abc.abstractmethod
    def consume(self) -> None:
        raise NotImplementedError
