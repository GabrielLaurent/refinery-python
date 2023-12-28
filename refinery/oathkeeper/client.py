import requests
import json

class OathkeeperClient:
    def __init__(self, oathkeeper_url):
        self.oathkeeper_url = oathkeeper_url

    def check_authorization(self, access_request):
        """Checks authorization with Oathkeeper.

        Args:
            access_request (dict): The access request data.

        Returns:
            dict: The Oathkeeper response.

        Raises:
            Exception: If the request fails.
        """
        try:
            response = requests.post(f'{self.oathkeeper_url}/decisions', json=access_request)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Oathkeeper request failed: {e}")


    def is_authorized(self, access_request):
        """Checks if the access request is authorized.
        Args:
            access_request (dict): The access request data.
        Returns:
            bool: True if authorized, False otherwise.
        """
        try:
            response = self.check_authorization(access_request)
            return response.get('allowed', False)
        except Exception as e:
            print(f"Error checking authorization: {e}") # Consider logging instead of printing.
            return False
