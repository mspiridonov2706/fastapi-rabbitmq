from pydantic import Field
from pydantic_settings import BaseSettings


# Название проекта. Используется в Swagger-документации
class ProjectSettings(BaseSettings):
    name: str = Field(default="auth_api", alias="PROJECT_NAME")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
