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
    """Get JSON data for a single occurrence.
    Must be an ID of one of your own observations"""

    url = f"{BASE_URL}/index.php/services/rest/occurrences/{observation_id}"
    try:
        response = requests.get(url, headers=headers(access_token))
    except Exception as err:
        logging.error(err)
        raise
    return response.json()


def create_observation(survey: int, doc: dict, access_token: str, trial: True) -> bool:
    """Create a new observation within a survey.

    survey (int) - an ID
    doc - the JSON which we are going to post. For now that's iRecord's internal format
    access token - Javascript Web Token that has permissions for a user account
    trial - whether this is a testing record. Assume, in the short term, thats the default.
    """
    suffix = "/index.php/services/rest/samples"
    try:
        response = requests.post(
            f"{BASE_URL}{suffix}", headers=headers(access_token), data=doc
        )

    except Exception as err:  # make narrower
        logging.error(err)
        raise
    return response


def get_surveys(access_token: str):
    suffix = "/index.php/services/rest/surveys"
    url = f"{BASE_URL}{suffix}"
    try:
        response = requests.get(url, headers=headers(access_token))
    except Exception as err:
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
    suffix = "/index.php/services/rest/projects"
    try:
        response = requests.get(f"{BASE_URL}{suffix}", headers=headers(access_token))
    except Exception as err:
        logging.error(err)
        raise

    return response
