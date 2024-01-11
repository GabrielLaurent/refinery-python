import requests

class OathkeeperClient:
    def __init__(self, oathkeeper_url):
        self.oathkeeper_url = oathkeeper_url

    def is_access_allowed(self, access_token, resource, action):
        """Validates access request against Oathkeeper.

        Args:
            access_token (str): The access token to validate.
            resource (str): The resource being accessed.
            action (str): The action being performed on the resource.

        Returns:
            bool: True if access is allowed, False otherwise.

        Raises:
            Exception: If there's an error communicating with Oathkeeper.
        """
        # Placeholder implementation
        # Replace with actual Oathkeeper API call
        try:
            # Construct the URL for the /decisions endpoint
            decisions_url = f'{self.oathkeeper_url}/decisions'

            # Include the access token and resource/action in the request headers or query parameters
            headers = {"Authorization": f"Bearer {access_token}"}
            params = {"resource": resource, "action": action}

            # Make a GET request to the /decisions endpoint
            response = requests.get(decisions_url, headers=headers, params=params)
            
            response.raise_for_status()

            # If Oathkeeper returns a 200 OK, access is allowed
            if response.status_code == 200:
                return True
            else:
                return False

        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Oathkeeper: {e}")
            return False # Or raise the exception, depending on desired behavior



    def introspect_token(self, access_token):
        """Introspects the provided access token using the /introspect endpoint.
        Args:
            access_token (str): The access token to introspect.
        Returns:
            dict: A dictionary containing the introspection results, or None if an error occurred.
        """
        try:
            introspect_url = f'{self.oathkeeper_url}/oauth2/introspect'
            data = {"token": access_token}
            response = requests.post(introspect_url, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Oathkeeper introspect endpoint: {e}")
            return None

if __name__ == '__main__':
    # Example usage (replace with your Oathkeeper URL and access token)
    oathkeeper_url = 'http://localhost:4456'  # Replace with your Oathkeeper Admin API URL
    access_token = 'valid-token'  # Replace with a valid access token
    resource = 'some-resource'
    action = 'read'

    client = OathkeeperClient(oathkeeper_url)

    is_allowed = client.is_access_allowed(access_token, resource, action)
    print(f"Access allowed: {is_allowed}")

    introspection_result = client.introspect_token(access_token)
    print(f"Token introspection result: {introspection_result}")