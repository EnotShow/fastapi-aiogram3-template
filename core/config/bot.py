import os

from pydantic.v1 import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class BotSettings(BaseSettings):
    token = os.environ.get("BOT_TOKEN")
    webhook_url = os.environ.get("WEBHOOK_URL")


settings_bot = BotSettings()
