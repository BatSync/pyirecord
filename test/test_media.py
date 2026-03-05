from pyirecord.media import media_queue


def test_media_queue(sample_media, jwt):
    """Upload an audio sample to iRecord
    Don't run this too often, as the media queue hangs around for at least a day
    and there doesn't seem to be a means of deleting uploads via the API
    """

    key = "sound"  # this can be arbitrary. the response uses it as a dict key

    filename_only = {key: str(sample_media)}

    doc = media_queue(filename_only, jwt)
    assert key in doc
    assert "tempPath" in doc[key]

    # Three-input style is in case we're reading from cloud storage, not local file
    file_object = {key: (str(sample_media), open(sample_media, "rb"), "media/x-wav")}

    doc = media_queue(file_object, jwt)
    assert key in doc
    assert "tempPath" in doc[key]
