import os
from dotenv import load_dotenv

load_dotenv()


class BotSettings:
    """
        Settings for telegram bot
    """
    
    __bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN")

    @property
    def bot_token(self):
        return self.__bot_token


fruct_settings = BotSettings()