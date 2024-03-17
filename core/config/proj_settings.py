import os

from pydantic.v1 import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    app_name: str = os.environ.get("APP_NAME")
    debug: bool = bool(os.environ.get("DEBUG"))
    secret_key: str = os.environ.get("SECRET_KEY")
    cors_allowed_origins: str = os.environ.get("CORS_ALLOWED_ORIGINS")
    version: str = "0.1"


settings = Settings()
