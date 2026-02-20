import os
from pyrecord.auth import jwt_token
from pyrecord.observations import get_projects
from dotenv import load_dotenv

load_dotenv()


def test_e2e():
    # ipdb.set_trace()
    t = jwt_token(os.environ.get("IRECORD_USER"), os.environ.get("IRECORD_PASSWD"))
    p = get_projects(t)
    print(p)
