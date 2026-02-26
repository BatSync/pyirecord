import os
from pyirecord.auth import jwt_token
from pyirecord.observations import (
    get_projects,
    get_docs,
    get_observation,
    create_observation,
)
from dotenv import load_dotenv

load_dotenv()


def test_e2e():
    t = jwt_token(os.environ.get("IRECORD_USER"), os.environ.get("IRECORD_PASSWD"))
    p = get_projects(t)
    print(p.url)
    print(p.content)


def test_doc():
    t = jwt_token(os.environ.get("IRECORD_USER"), os.environ.get("IRECORD_PASSWD"))
    d = get_docs(t)
    print(d.url)
    print(d.content)


def test_obs(sample_record):
    t = jwt_token(os.environ.get("IRECORD_USER"), os.environ.get("IRECORD_PASSWD"))
    d = get_observation(38001839, access_token=t)
    print(d.url)
    print(d.content)

    c = create_observation(1, sample_record, access_token=t)
    print(c.url)
    print(c.content)
