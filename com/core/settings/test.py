import os
from pathlib import Path
import dotenv
from .base import *

# ================= TEST SETTINGS ====================
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print("base dir test", BASE_DIR)
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# ============== LOAD CUSTOM ENV FILE ================
dotenv_file = os.path.join(BASE_DIR, ".test.env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file, override=True)  # need to override default env values


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_database',
    }
}


SECRET_TEST_EMAIL = os.getenv("SECRET_TEST_EMAIL")
SECRET_TEST_PWD = os.environ.get("SECRET_TEST_PWD")
