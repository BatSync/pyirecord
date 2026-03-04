import requests
import logging
from pyirecord import BASE_URL
from pyirecord.http import headers

logging.basicConfig(level=logging.INFO)


def validate_params(**params):
    """Check our generic dictionary of search parameters uses good terms."""
    # This one is required
    if "taxon_list_id" not in params:
        params["taxon_list_id"] = default_taxon_list()

    # TODO add any more rules (e.g. about matching terms in lists) if needed
    # Delete any keys not appearing in the list
    return params


def default_taxon_list():
    """If the query does not specify a taxon_list_id, use a default.
    15 is the UK Species Inventory.
    Note its encoded as string type in the JSON back and forth
    """
    return "15"


def taxa_search(access_token: str, **params):
    """Searches taxonomy to find a number ID to use creating occurrences.
    Any named arguments are passed through to the search query, validated first.
    See https://warehouse1.indicia.org.uk/index.php/services/rest#collapse-19
    (We could spell them all out here, with default None values)

    Without arguments other than auth token, returns 100 random records from
    the UK Species Inventory
    """

    suffix = "/index.php/services/rest/taxa/search"
    url = f"{BASE_URL}{suffix}"
    params = validate_params(**params)
    try:
        response = requests.get(url, headers=headers(access_token), params=params)
    except Exception as err:
        logging.error(err)
        raise

    response.raise_for_status()
    result = response.json()
    data = []
    if "data" in result and len(result["data"]):
        data = result["data"]

    return data
