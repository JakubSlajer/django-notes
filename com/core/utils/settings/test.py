import os

from core.settings import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

dotenv_file = os.path.join(BASE_DIR, ".test.env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


SECRET_TEST_EMAIL = os.environ.get("SECRET_TEST_EMAIL")
SECRET_TEST_PWD = os.environ.get("SECRET_TEST_PWD")

print(SECRET_TEST_EMAIL)
print(SECRET_TEST_PWD)