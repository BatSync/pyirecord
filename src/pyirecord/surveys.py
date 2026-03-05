import requests
import logging
from pyirecord.http import headers, BASE_URL


def get_surveys(access_token: str):
    """Returns a raw list of surveys accessible to the current user"""
    suffix = "/index.php/services/rest/surveys"
    url = f"{BASE_URL}{suffix}"
    try:
        response = requests.get(url, headers=headers(access_token))
    except Exception as err:
        logging.error(err)
        raise
    return response.json()


def survey_id(name: str, access_token: str):
    """Given a readable name, return an ID from the Indicia API"""
    survey_id = None
    surveys = get_surveys(access_token)
    matches = list(filter(lambda x: x["values"]["title"] == name, surveys))
    if len(matches) == 0:
        logging.info("Could not match this survey name to an ID")
    else:
        survey_id = matches[0]["values"]["id"]
    return survey_id
