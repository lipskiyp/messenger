"""
Default app and database configuration.
"""

from os import environ
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Default FastAPI App and PostgreSQL settings.
    """
    APP_HOST: str = environ.get("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(environ.get("APP_PORT", 8080))

    POSTGRES_DB: str = environ.get("POSTGRES_DB", "postgres")
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "pswrd")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "db")
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", 5432))

    class Config:
        env_file = './.env'

    def get_db_url(self) -> str:
        """
        Get PostgreSQL url.
        """
        print(f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}")
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings: Settings = Settings()
