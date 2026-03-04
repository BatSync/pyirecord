import requests
import os
import logging
from typing import Optional
from dotenv import load_dotenv
from pyirecord.http import headers

logging.basicConfig(level=logging.INFO)

load_dotenv()

BASE_URL = os.environ.get("IRECORD_BASE_URL", "https://irecord.org.uk")


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
    return response


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


def attributes(access_token: str) -> dict:
    """Get identifiers and brief metadata for all "occurrence attributes"
    - think of these as controlled tags"""
    suffix = "/index.php/services/rest/occurrence-attributes-websites"
    try:
        response = requests.get(f"{BASE_URL}{suffix}", headers=headers(access_token))
    except Exception as err:
        logging.error(err)
        raise

    response.raise_for_status()
    # Raw response is raw - list where every item has a single key, 'values'
    # Transform it into a dict with IDs for keys

    return {x["values"]["id"]: x["values"] for x in response.json()}


def attribute_terms(attr_id: int, access_token: str):
    """Find out more about the values we can use with an attribute, given its ID"""
    suffix = "/index.php/services/rest/occurrence-attributes"
    try:
        response = requests.get(
            f"{BASE_URL}{suffix}/{attr_id}", headers=headers(access_token)
        )
    except Exception as err:
        logging.error(err)
        raise

    response.raise_for_status()
    return response.json()
