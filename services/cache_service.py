from os import path

from services.config_service import ConfigService


class CacheService:
    cache = []

    def __init__(self, config: ConfigService):
        self.path = "cache.log"
        print(f"Log file: {path.abspath(self.path)}")
        if path.isfile(self.path):
            with open(self.path, "r") as f:
                self.cache = f.readlines()
        else:
            self.cache = []

    def add(self, entry: str):
        self.cache.append(f"{entry}\n")

    def has(self, entry: str):
        return f"{entry}\n" in self.cache

    def save(self):
        while len(self.cache) > 100:
            self.cache.pop(0)
        f = open(self.path, "w")
        f.writelines(self.cache)
        f.close()
