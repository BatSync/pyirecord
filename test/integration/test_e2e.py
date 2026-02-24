import os
from pyirecord.auth import jwt_token
from pyirecord.observations import get_projects, get_docs
from dotenv import load_dotenv

load_dotenv()


def test_e2e():
    t = jwt_token(os.environ.get("IRECORD_USER"), os.environ.get("IRECORD_PASSWD"))
    p = get_projects(t)
    print(p)


def test_doc():
    t = jwt_token(os.environ.get("IRECORD_USER"), os.environ.get("IRECORD_PASSWD"))
    print(t)
    d = get_docs(t)
    print(d)
