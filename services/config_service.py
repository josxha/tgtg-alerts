import os


class ConfigService:
    def __init__(self):
        # too good to go
        if 'TGTG_EMAIL' in os.environ:
            self.email = os.environ['TGTG_EMAIL']
        if 'TGTG_ACCESS_TOKEN' in os.environ:
            self.access_token = os.environ['TGTG_ACCESS_TOKEN']
        if 'TGTG_REFRESH_TOKEN' in os.environ:
            self.refresh_token = os.environ['TGTG_REFRESH_TOKEN']
        if 'TGTG_USER_ID' in os.environ:
            self.user_id = os.environ['TGTG_USER_ID']
        if 'TGTG_COOKIE' in os.environ:
            self.cookie = os.environ['TGTG_COOKIE']
        # telegram
        if 'TELEGRAM_BOT_TOKEN' in os.environ:
            self.tg_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
        if 'TELEGRAM_CHAT_ID' in os.environ:
            self.tg_chat_id = os.environ['TELEGRAM_CHAT_ID']

    def has_token(self) -> bool:
        return self.access_token is not None and self.access_token != "" \
            and self.refresh_token is not None and self.refresh_token != "" \
            and self.user_id is not None and self.user_id != "" \
            and self.cookie is not None and self.cookie != ""
