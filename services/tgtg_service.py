from tgtg import TgtgClient

from services.config_service import ConfigService


class TgtgService:
    def __init__(self, config: ConfigService):
        self.client = None
        if not config.has_token():
            self.client = TgtgClient(email=config.email)
            credentials = self.client.get_credentials()
            print(credentials)
            exit(0)
        self.client = TgtgClient(
            access_token=config.access_token,
            refresh_token=config.refresh_token,
            user_id=config.user_id,
            cookie=config.cookie)

    def get_items(self):
        return self.client.get_items()
