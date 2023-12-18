import time

class CacheManager:
    def __init__(self, default_expiration=60):
        self.cache = {}
        self.default_expiration = default_expiration

    def get(self, key):
        if key in self.cache:
            value, expiration = self.cache[key]
            if expiration is None or expiration > time.time():
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key, value, expiration=None):
        if expiration is None:
            expiration = time.time() + self.default_expiration
        self.cache[key] = (value, expiration)

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        self.cache = {}
