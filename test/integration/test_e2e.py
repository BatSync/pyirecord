"""An end-to-end test of creating a new record"""

from pyirecord.observations import create_observation
from pyirecord.media import media_queue
from pyirecord.surveys import survey_id


# All these default inputs are created in conftest.py
def test_e2e(sample_record, survey_name, sample_media, jwt):
    # Find the ID of our survey. Can be configured in env variables
    s_id = survey_id(survey_name, jwt)
    sample_record["values"]["survey_id"] = s_id

    # Upload a media sample and get back a temporary path to attach to record
    media = media_queue({"sound": sample_media}, jwt)
    print(media)

    # This could be 'tempPath'? But examples look like value of 'name'
    media_path = media["sound"]["name"]

    sample_record["media"] = [
        {
            "values": {"queued": media_path, "caption": "Sample image"},
        }
    ]

    # TODO add occurrence or sample attributes after we set up a survey
    c = create_observation(s_id, sample_record, access_token=jwt)
    print(c)
