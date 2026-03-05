import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ.get("IRECORD_BASE_URL", "https://irecord.org.uk")


def headers(access_token: str):
    """Set the headers to authenticate with our"""
    # Set the authorisation header to USER:[client system ID]:SECRET:[secret]
    return {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}
