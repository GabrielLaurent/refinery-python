# examples/auth_flow.py

from refinery.kratos.client import KratosClient
from refinery.oathkeeper.client import OathkeeperClient

# Example usage (replace with actual values)
kratos_client = KratosClient(kratos_url='http://localhost:4433')
oathkeeper_client = OathkeeperClient(oathkeeper_url='http://localhost:4456')  # Updated URL

user_id = 'user123'
session_token = 'sessionToken123'
resource = 'protected-resource'
action = 'read'

# Validate session with Kratos
#user = kratos_client.get_user(user_id)
#is_session_valid = kratos_client.validate_session(session_token)

# Check authorization with Oathkeeper
is_authorized = oathkeeper_client.is_authorized(session_token, resource, action)

if is_authorized:
    print('User is authorized.')
else:
    print('User is not authorized.')