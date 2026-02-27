import pytest
from pyirecord.auth import jwt_token
import os


@pytest.fixture
def sample_record():
    """https://indicia-docs.readthedocs.io/en/latest/developing/rest-web-services/resources.html#index-php-services-samples"""  # noqa: E501
    return {
        "values": {
            "survey_id": 1,
            "entered_sref": "SU1234",
            "entered_sref_system": "OSGB",
            "date": "01/08/2020",
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
