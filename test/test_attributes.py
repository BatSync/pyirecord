from pyirecord.surveys import survey_id
from pyirecord.attributes import attributes


def test_attrs(jwt):
    # Search for all attributes we have permissions to create
    attrs = attributes(jwt)
    assert attrs

    # Search for attributes pertaining to a survey
    s_id = survey_id("iRecord Bats", jwt)

    attrs = attributes(jwt, survey_id=s_id)
    assert attrs
    k = next(iter(attrs))
    assert k == attrs[k]["id"]

    # Default to occurrence attributes; samples are the same format
    attrs = attributes(jwt, attribute_type="sample", survey_id=s_id)
    assert attrs
    k = next(iter(attrs))
    assert k == attrs[k]["id"]
