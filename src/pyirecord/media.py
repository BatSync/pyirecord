import requests
import os
import logging
import mimetypes
from dotenv import load_dotenv
from pyirecord.http import headers

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

BASE_URL = os.environ.get("IRECORD_BASE_URL", "https://irecord.org.uk")


class MediaError(Exception):
    pass


def media_queue(files: dict, access_token: str):
    """
    Post audio or other media to a queue, to attach later to an observation.
    Each _value_ in the files dictionary should be either

    * a filename (str)
    * a tuple (filename, open file-like object, mime type)

    {'sound': str or tuple,
     'photo': str or tuple}

    The keys can have arbitrary names - choose ones you'll remember!
    https://warehouse1.indicia.org.uk/index.php/services/rest#collapse-2

    Tuple interface is needed for this API - it's picky about MIME types.
    Filenames can be supplied, but in some use cases we don't have a local file
    (e.g. we are reading observation media from s3 storage) - support both inputs.
    """

    url = f"{BASE_URL}/index.php/services/rest/media-queue"

    # TODO validate the input? (Check image/sound formats, length and types if tuple)

    for k, f in files.items():
        if isinstance(f, str):
            mimetype = mimetypes.guess_type(f)[0]
            # MIME type gets used as file suffix in the queue. We can't not specify it.
            # For avoidance of doubt, remove x- prefix (for audio files)
            try:
                mimetype = mimetype.replace("x-", "")
            except AttributeError as err:
                raise MediaError(err)

            files[k] = (f, open(f, "rb"), mimetype)

    print(files)
    h = headers(access_token)
    del h["Accept"]

    try:
        response = requests.post(url, headers=h, files=files)
    except Exception as err:
        logging.error(err)
        raise

    response.raise_for_status()
    return response.json()
