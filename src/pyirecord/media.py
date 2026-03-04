import requests
import os
import logging
from dotenv import load_dotenv
from pyirecord.http import headers

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

BASE_URL = os.environ.get("IRECORD_BASE_URL", "https://irecord.org.uk")


def media_queue(files: dict, access_token: str):
    """
    Post audio or other media to a queue, to attach later to an observation.
    Input should be

    {'sound': bytes,
     'photo': bytes}

    Where we _assume_ the keys can have arbitrary names - choose useful ones!
    They get re-used as JSON dictionary keys in the response.

    https://warehouse1.indicia.org.uk/index.php/services/rest#collapse-2
    """

    url = f"{BASE_URL}/index.php/services/rest/media-queue"

    # TODO validate the file formats? (Check image formats, header tags etc?)
    logging.debug(files)    
    try:
        response = requests.post(url, headers=headers(access_token), files=files)
    except Exception as err:
        logging.error(err)
        raise

    response.raise_for_status()
    return response
