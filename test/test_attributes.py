from pyirecord.surveys import survey_id
from pyirecord.attributes import attributes


def test_attrs(jwt):
    # Search for all attributes we have permissions to create
    attrs = attributes(jwt)
    assert attrs

    # Search for attributes pertaining to a survey
    s_id = survey_id("iRecord Bats", jwt)
    print(s_id)
    attrs = attributes(jwt, survey_id=s_id)
    assert attrs
    # dump data to compare with iRecord devs
    for k, v in attrs.items():
        print(v["id"], v["caption"])
