from pyirecord.observations import create_observation, attributes
from pyirecord.surveys import survey_id


def test_attrs(jwt):
    print(attributes(jwt))


def test_create(sample_record, jwt):
    s_id = survey_id("iRecord Bats", jwt)
    sample_record["values"]["survey_id"] = s_id
    c = create_observation(s_id, sample_record, access_token=jwt)
    print(c.url)
    print(c.content)
