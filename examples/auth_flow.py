import asyncio
import os

from refinery.kratos.client import KratosClient
from refinery.oathkeeper.client import OathkeeperClient


async def main():
    kratos_admin_url = os.getenv("KRATOS_ADMIN_URL", "http://localhost:4434")
    oathkeeper_url = os.getenv("OATHKEEPER_URL", "http://localhost:4456")

    kratos_client = KratosClient(kratos_admin_url)
    oathkeeper_client = OathkeeperClient(oathkeeper_url)

    # Example: Validate a Kratos session
    session_token = "your_session_token"  # Replace with a real session token
    try:
        session = await kratos_client.get_session(session_token)
        print(f"Session is valid for user: {session.identity.id}")
    except Exception as e:
        print(f"Session validation failed: {e}")

    # Example: Check access using Oathkeeper
    access_token = "your_access_token" # Replace with a valid access token or omit if using cookies
    subject = "your_subject"  # Usually the user ID
    access_url = os.getenv("ACCESS_URL", "http://localhost:4455/protected")  # Adjust as needed.

    try:
        decision = await oathkeeper_client.decide(access_url, subject, token=access_token)
        if decision:
            print("Access GRANTED")
        else:
            print("Access DENIED")
    except Exception as e:
        print(f"Access request failed: {e}")


if __name__ == "__main__":
    asyncio.run(main())