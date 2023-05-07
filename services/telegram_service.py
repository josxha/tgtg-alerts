from telegram import Bot

from services.config_service import ConfigService


class TelegramService:
    def __init__(self, config: ConfigService):
        self.chat_id = config.tg_chat_id
        self.bot = Bot(config.tg_bot_token)

    async def send_message(self, message: str):
        print(f"Sending telegram message...\n{message}")
        await self.bot.send_message(chat_id=self.chat_id, text=message)
