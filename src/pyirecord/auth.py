import os
import logging
import httpx
from urllib.parse import parse_qs

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
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
    logging.info(
      "iRecord OAuth configuration: "
      "token_url=%s, client_id_present=%s, client_secret_present=%s",
      IRECORD_TOKEN_URL,
      bool(IRECORD_CLIENT_ID),
      bool(IRECORD_CLIENT_SECRET),
    )
    if not IRECORD_CLIENT_ID or not IRECORD_CLIENT_SECRET:
        raise ClientException(
            "No credentials for iRecord client found. "
            "Please set IRECORD_CLIENT_ID and "
            "IRECORD_CLIENT_SECRET in a file named .env"
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
            sent_form = parse_qs(response.request.content.decode("utf-8"))

            logging.info(
              "iRecord request diagnostic, data sent to auth server: IRECORD_TOKEN_URL=%s, " + \
              "IRECORD_CLIENT_ID=%s, IRECORD_CLIENT_SECRET=%s, headers=%s",
              IRECORD_TOKEN_URL, IRECORD_CLIENT_ID, IRECORD_CLIENT_SECRET, headers
            )

            logging.info(
                "Further iRecord request diagnostic: content_type=%s, form_keys=%s, grant_type=%s",
                response.request.headers.get("content-type"),
                sorted(sent_form.keys()),
                sent_form.get("grant_type", [None])[0],
            )
            
            response.raise_for_status()
            token_info = response.json()
        except httpx.HTTPStatusError as e:
            logging.error(
                "iRecord OAuth error: status=%s, response=%s",
                e.response.status_code,
                e.response.text
            )
            raise

        except Exception:
            logging.exception("Unexpected iRecord authentication error")
            raise
          
    return token_info.get("access_token")
