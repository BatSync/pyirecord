"""An end-to-end test of creating a new record"""

from pyirecord.observations import (
    create_observation,
)

from pyirecord.surveys import survey_id


def test_e2e(sample_record, survey_name, jwt):
    # Find the ID of our survey. Can be configured in env variables
    s_id = survey_id(survey_name, jwt)
    sample_record["values"]["survey_id"] = s_id

    # Upload a media sample and get back a temporary path to attach to record

    c = create_observation(s_id, sample_record, access_token=jwt)
    print(c.url)
    print(c.content)
