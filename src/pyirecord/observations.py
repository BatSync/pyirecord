import requests
import logging
from typing import Optional
from pyirecord.http import headers, BASE_URL

logging.basicConfig(level=logging.INFO)


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


def create_observation(
    survey: int, doc: dict, access_token: str, trial: Optional[bool] = True
) -> bool:
    """Create a new observation within a survey.

    survey (int) - an ID
    doc - the JSON which we are going to post. For now that's iRecord's internal format
    access token - Javascript Web Token that has permissions for a user account
    trial - whether this is a testing record. Assume, in the short term, thats the default.
    """
    suffix = "/index.php/services/rest/samples"
    h = headers(access_token)
    try:
        response = requests.post(f"{BASE_URL}{suffix}", headers=h, json=doc)

    except Exception as err:  # make narrower
        logging.error(err)
        raise
    return response.json()


def get_docs(access_token: str) -> str:
    suffix = "/index.php/services/rest/"
    h = headers(access_token)
    # It only returns HTML and you have to ask for that explicit like
    h["Accept"] = "text/html"
    try:
        response = requests.get(f"{BASE_URL}{suffix}", headers=h)
    except Exception as err:
        logging.error(err)
        raise

    response.raise_for_status()

    # Just give back the document. Better than a no-op
    return str(response.content)
