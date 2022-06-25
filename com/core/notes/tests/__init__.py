# load custom environment properties specially for this module tests
import os
import dotenv
from pathlib import Path

# ================= TEST SETTINGS ====================
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

# ============== LOAD CUSTOM ENV FILE ================
dotenv_file = os.path.join(BASE_DIR, "resources/.test.env")
print(dotenv_file)
if os.path.isfile(dotenv_file):
    print("found test env!")
    dotenv.load_dotenv(dotenv_file, override=True) # need to override default env values
    print(f"overriding env with {dotenv_file}")