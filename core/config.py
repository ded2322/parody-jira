from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: str

    HOST_DB: str
    PORT_DB: int
    NAME_DB: str
    PASS_DB: str
    USER_DB: str


    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.USER_DB}:{self.PASS_DB}@{self.HOST_DB}:{self.PORT_DB}/{self.NAME_DB}"

    HOST_DB_TEST: str
    PORT_DB_TEST: int
    NAME_DB_TEST: str
    PASS_DB_TEST: str
    USER_DB_TEST: str

    @property
    def DATABASE_URL_TEST(self):
        return f"postgresql+asyncpg://{self.USER_DB_TEST}:{self.PASS_DB_TEST}@{self.HOST_DB_TEST}:{self.PORT_DB_TEST}/{self.NAME_DB_TEST}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
