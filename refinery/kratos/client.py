import httpx

class KratosClient:
    def __init__(self, kratos_admin_url):
        self.kratos_admin_url = kratos_admin_url
        self.client = httpx.AsyncClient(base_url=self.kratos_admin_url)

    async def validate_session(self, session_token: str) -> dict:
        """Validates a Kratos session using the session token.

        Args:
            session_token: The Kratos session token.

        Returns:
            A dictionary containing session information if the session is valid.

        Raises:
            httpx.HTTPStatusError: If the Kratos Admin API returns an error.
            Exception: If any other error occurs during session validation.
        """
        url = "/sessions/whoami"
        headers = {"Cookie": f"ory_kratos_session={session_token}"}
        try:
            response = await self.client.get(url, headers=headers)
            response.raise_for_status()  # Raise HTTPStatusError for bad responses (4xx or 5xx)
            return response.json()
        except httpx.HTTPStatusError as e:
            # Handle specific HTTP errors from Kratos
            print(f"Kratos session validation error: {e}") # Add logging
            raise  # Re-raise the exception to be handled by the caller
        except Exception as e:
            print(f"An unexpected error occurred during Kratos session validation: {e}") # Add logging
            raise Exception(f"Failed to validate Kratos session: {e}") from e


    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()