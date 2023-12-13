from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# Название проекта. Используется в Swagger-документации
class RabbitMQSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="rabbit_mq_")

    protocol: str = Field(default="amqp", alias="protocol")
    login: str = Field(default="guest", alias="login")
    password: str = Field(default="guest", alias="password")
    host: str = Field(default="rabbitmq", alias="host")
    port: int = Field(default=5672, alias="port")

    @property
    def dsn(self) -> str:
        return f"{self.protocol}://{self.login}:{self.password}@{self.host}:{self.port}"
