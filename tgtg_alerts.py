#!/usr/bin/env python
from services.cache_service import CacheService
from services.config_service import ConfigService
from services.telegram_service import TelegramService
from services.tgtg_service import TgtgService
import asyncio


class TgtgAlerts:
    def __init__(self):
        self.config = ConfigService()
        self.tgtg = TgtgService(self.config)
        self.telegram = TelegramService(self.config)
        self.cache = CacheService(self.config)

    async def currently_available(self):
        print("List currently available")
        items = self.tgtg.get_items()
        message = ""
        for item in items:
            items_available = item['items_available']
            if items_available == 0:
                continue
            message += f"{item['display_name']}: {items_available} verfügbar\n"
        if message == "":
            message = "Derzeit sind keine Angebote verfügbar."
        await self.telegram.send_message(message)

    async def new_available(self):
        print("Get new offers")
        items = self.tgtg.get_items()
        for item in items:
            id = item['item']['item_id']
            if self.cache.has(id):
                continue
            message = f"{item['display_name']}: {item['items_available']} verfügbar"
            await self.telegram.send_message(message)
            self.cache.add(id)
        self.cache.save()


if __name__ == "__main__":
    app = TgtgAlerts()
    asyncio.run(app.new_available())
