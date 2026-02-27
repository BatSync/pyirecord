from pyirecord.surveys import survey_id


def test_survey_id(jwt):
    s_id = survey_id("iRecord Bats", jwt)
    assert s_id is not None
    print(s_id)
