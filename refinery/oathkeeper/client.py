# refinery/oathkeeper/client.py
import requests

class OathkeeperClient:
    def __init__(self, oathkeeper_url):
        self.oathkeeper_url = oathkeeper_url

    def is_authorized(self, access_token, resource, action):
        # Placeholder for Oathkeeper authorization logic
        try:
            response = requests.get(f'{self.oathkeeper_url}/decisions')  # Simulate the /decisions endpoint
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.status_code == 200 #Simulate return code
        except requests.exceptions.RequestException as e:
            return False
    
    # Add more methods as needed