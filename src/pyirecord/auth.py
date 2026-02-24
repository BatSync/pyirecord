import os
import logging
import httpx

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.DEBUG)
IRECORD_TOKEN_URL = os.environ.get(
    "IRECORD_TOKEN_URL", "https://irecord.org.uk/oauth/token"
)
IRECORD_CLIENT_ID = os.environ.get("IRECORD_CLIENT_ID", "")
IRECORD_CLIENT_SECRET = os.environ.get("IRECORD_CLIENT_SECRET", "")


class ClientException(Exception):
    pass


def token_data(client_id: str, username: str, password: str) -> dict:
    # Exchange code for token
    return {
        "client_id": client_id,
        "username": username,
        "password": password,
        "grant_type": "password",
        "scope": "",
    }


def check_client():
    if not IRECORD_CLIENT_ID or not IRECORD_CLIENT_ID:
        raise ClientException(
            "No credentials for iRecord client found. Please set IRECORD_CLIENT_ID and IRECORD_CLIENT_SECRET in a file named .env"
        )


def jwt_token(username: str, password: str):
    """Use password grant type to obtain a JWT token that lets us act as the user.
    This OAuth2 method is deprecated as potentially insecure, but it's what iRecord offers.
    """

    check_client()
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    with httpx.Client() as client:
        try:
            response = client.post(
                IRECORD_TOKEN_URL,
                data=token_data(IRECORD_CLIENT_ID, username, password),
                auth=(IRECORD_CLIENT_ID, IRECORD_CLIENT_SECRET),
                headers=headers,
            )
            response.raise_for_status()
            token_info = response.json()
        except Exception as e:
            print(e)
            raise
    return token_info.get("access_token")
