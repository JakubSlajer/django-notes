import os
from pathlib import Path
import dotenv
from .base import *

# ================= TEST SETTINGS ====================
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# ============== LOAD CUSTOM ENV FILE ================
dotenv_file = os.path.join(BASE_DIR, ".test.env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file, override=True)  # need to override default env values


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_database',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


SECRET_TEST_EMAIL = os.getenv("SECRET_TEST_EMAIL")
SECRET_TEST_PWD = os.environ.get("SECRET_TEST_PWD")
