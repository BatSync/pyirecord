import requests
import logging
from pyirecord import BASE_URL
from pyirecord.http import headers

logging.basicConfig(level=logging.INFO)


def taxa_search(access_token: str):
    """Returns a raw list of surveys accessible to the current user"""
    suffix = "/index.php/services/data/taxa_search"
    url = f"{BASE_URL}{suffix}"
    # TODO figure out how we supply a name as query param - see notes.md
    try:
        response = requests.get(url, headers=headers(access_token))
    except Exception as err:
        logging.error(err)
        raise
    return response
