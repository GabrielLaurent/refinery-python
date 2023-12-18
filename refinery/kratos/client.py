import ory_kratos_client
from ory_kratos_client.api import identity_api
from refinery.cache.cache_manager import CacheManager

class KratosClient:
    def __init__(self, kratos_url, cache_expiration=60):
        self.kratos_url = kratos_url
        self.configuration = ory_kratos_client.Configuration(host=kratos_url)
        self.api_client = ory_kratos_client.ApiClient(self.configuration)
        self.identity_api = identity_api.IdentityApi(self.api_client)
        self.cache_manager = CacheManager(default_expiration=cache_expiration)

    def get_identity(self, identity_id):
        cached_identity = self.cache_manager.get(identity_id)
        if cached_identity:
            return cached_identity

        try:
            api_response = self.identity_api.get_identity(id=identity_id)
            self.cache_manager.set(identity_id, api_response)
            return api_response
        except ory_kratos_client.ApiException as e:
            print(f"Exception when calling IdentityApi->get_identity: {e}\n")
            return None
