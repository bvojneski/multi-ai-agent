import os
from dotenv import load_dotenv

load_dotenv(override=True)

MODEL = os.getenv("MODEL")
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")