import requests
import os

BASE_URL = os.environ.get("IRECORD_BASE_URL", "https://irecord.org.uk/")


def headers(access_token: str):
    return {"Authorization": f"Bearer {access_token}"}


def get_observation(observation_id: int, access_token: str):
    try:
        response = requests.get(f"{BASE_URL}/???")
    except Exception:
        raise
    return response


def get_projects(access_token: str):
    for suffix in ("/projects", "/rest/projects", "/index.php/rest/projects"):
        response = requests.get(f"{BASE_URL}{suffix}", headers=headers(access_token))
        print(response)
