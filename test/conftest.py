import pytest
from pyirecord.auth import jwt_token
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def sample_record():
    """https://indicia-docs.readthedocs.io/en/latest/developing/rest-web-services/resources.html#index-php-services-samples"""  # noqa: E501
    """Replace s_id with the survey you are posting to"""
    return {
        "values": {
            "survey_id": "{s_id}",
            "entered_sref": "SU1234",
            "entered_sref_system": "OSGB",
            "date": "01/08/2026",
        },
        "occurrences": [
            {
                "values": {
                    "taxa_taxon_list_id": 2,
                    "occAttr:8": "4 adults",
                },
            }
        ],
    }


@pytest.fixture
def jwt():
    return jwt_token(os.environ.get("IRECORD_USER"), os.environ.get("IRECORD_PASSWD"))


@pytest.fixture
def sample_id():
    """An occurrence ID in iRecord. Defaults to one of JW's"""
    return os.environ.get("TEST_SAMPLE_ID", 38001839)
