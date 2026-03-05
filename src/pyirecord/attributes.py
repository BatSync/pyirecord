import requests
import logging
from pyirecord.http import headers, BASE_URL


def attributes(access_token: str) -> dict:
    """Get identifiers and brief metadata for all "occurrence attributes"
    - think of these as controlled tags"""
    suffix = "/index.php/services/rest/occurrence-attributes"
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
