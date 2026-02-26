import requests
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

BASE_URL = os.environ.get("IRECORD_BASE_URL", "https://irecord.org.uk")


def headers(access_token: str):
    """Set the headers to authenticate with our"""
    # Set the authorisation header to USER:[client system ID]:SECRET:[secret]
    h = {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}
    logging.debug(h)
    return h


def get_observation(observation_id: int, access_token: str):
    url = f"{BASE_URL}/index.php/services/occurrences/{observation_id}"
    try:
        response = requests.get(url)
    except Exception as err:
        logging.error(err)
        raise
    return response


def create_observation(survey: int, doc: dict, access_token: str) -> bool:
    suffix = "/index.php/services/rest/samples"
    try:
        response = requests.post(
            f"{BASE_URL}{suffix}", headers=headers(access_token), data=doc
        )

    except Exception as err:  # make narrow
        logging.error(err)
        raise
    return response


def get_projects(access_token: str):
    suffix = "/index.php/services/rest/projects"
    url = f"{BASE_URL}{suffix}"
    try:
        response = requests.get(url, headers=headers(access_token))
    except Exception as err:
        logging.error(err)
        raise
    return response


def get_docs(access_token: str):
    suffix = "/index.php/services/rest"
    try:
        response = requests.get(f"{BASE_URL}{suffix}", headers=headers(access_token))
    except Exception as err:
        logging.error(err)
        raise

    return response
