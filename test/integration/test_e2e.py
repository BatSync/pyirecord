"""Integration tests that are a bit of a kludge -
Hardcode a record name so they're limited to Jo's user.
For interface development - replace or refine later"""

from pyirecord.observations import (
    get_docs,
    get_observation,
    create_observation,
)

from pyirecord.surveys import survey_id, get_surveys


def test_e2e(jwt):
    surveys = get_surveys(jwt)
    assert len(surveys)
    assert "values" in surveys[0]


def test_doc(jwt):
    doc = get_docs(jwt)
    # check for presence of arbitrary string in API docs (HTML only)
    assert "endpoint" in str(doc)


def test_obs(jwt, sample_id):
    d = get_observation(sample_id, access_token=jwt)
    assert "values" in d
    # int ID comes back as string type
    assert d["values"]["id"] == str(sample_id)


def test_create(sample_record, jwt):
    s_id = survey_id("iRecord Bats", jwt)
    c = create_observation(s_id, sample_record, access_token=jwt)
    print(c.url)
    print(c.content)
