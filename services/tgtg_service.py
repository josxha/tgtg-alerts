from tgtg import TgtgClient

from services.config_service import ConfigService


class TgtgService:
    def __init__(self, config: ConfigService):
        self.client = None
        if not config.has_token():
            if config.email is None or config.email == "":
                print("Please set the TGTG_EMAIL environment variable to get a new session or the other TGTG_* "
                      "variables with your session.")
                exit(1)
            self.client = TgtgClient(email=config.email)
            credentials = self.client.get_credentials()
            print(f"TGTG_ACCESS_TOKEN:\n{credentials['access_token']}\n\n"
                  f"TGTG_REFRESH_TOKEN:\n{credentials['refresh_token']}\n\n"
                  f"TGTG_USER_ID:\n{credentials['TGTG_USER_ID']}\n\n"
                  f"TGTG_COOKIE:\n{credentials['TGTG_COOKIE']}\n")
            exit(0)
        self.client = TgtgClient(
            access_token=config.access_token,
            refresh_token=config.refresh_token,
            user_id=config.user_id,
            cookie=config.cookie)

    def get_items(self):
        return self.client.get_items()
