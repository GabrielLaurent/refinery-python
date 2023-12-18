import requests
from refinery.cache.cache_manager import CacheManager
import json

class OathkeeperClient:
    def __init__(self, oathkeeper_url, cache_expiration=60):
        self.oathkeeper_url = oathkeeper_url
        self.cache_manager = CacheManager(default_expiration=cache_expiration)

    def check_access_request(self, access_request):
        cache_key = json.dumps(access_request)
        cached_result = self.cache_manager.get(cache_key)
        if cached_result:
            return cached_result

        try:
            response = requests.post(self.oathkeeper_url + '/decisions', json=access_request)
            if response.status_code == 200:
                self.cache_manager.set(cache_key, True)
                return True
            else:
                self.cache_manager.set(cache_key, False)
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error during access request: {e}")
            return False
