import requests
import os

from typing import Optional


class KratosClient:
    def __init__(self, kratos_admin_url: str = None):
        self.kratos_admin_url = kratos_admin_url or os.environ.get("KRATOS_ADMIN_URL")
        if not self.kratos_admin_url:
            raise ValueError("Kratos Admin URL is required.")

        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get_user(self, session_token: str = None, user_id: str = None) -> Optional[dict]:
        """Retrieves user information from Kratos based on a session token or user ID.

        Args:
            session_token: The Kratos session token.
            user_id: The Kratos user ID.

        Returns:
            A dictionary containing the user's identity data, or None if not found.
        """
        if session_token:
            try:
                response = self.session.get(
                    f"{self.kratos_admin_url}/sessions/whoami",
                    headers={"Cookie": f"ory_kratos_session={session_token}"},
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error retrieving user by session token: {e}")
                return None
        elif user_id:
            try:
                response = self.session.get(f"{self.kratos_admin_url}/identities/{user_id}")
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error retrieving user by user ID: {e}")
                return None
        else:
            print("Either session_token or user_id must be provided.")
            return None
