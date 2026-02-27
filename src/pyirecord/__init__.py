import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.environ.get("IRECORD_BASE_URL", "https://irecord.org.uk")
