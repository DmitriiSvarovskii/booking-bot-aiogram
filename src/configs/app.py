from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: str

    BOT_TOKEN: str

    WEBAPP_URL: str

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    SERVICE_URL: str

    @property
    def DB_URL(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8')


settings = Settings()
