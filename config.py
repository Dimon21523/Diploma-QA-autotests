import os
from dotenv import load_dotenv

load_dotenv()

URL_UI = os.getenv("URL_UI", "")
API_BASE_URL = os.getenv("API_BASE_URL", "")
USER_LOGIN = os.getenv("USER_LOGIN", "")
USER_PASSWORD = os.getenv("USER_PASSWORD", "")
API_TOKEN = os.getenv("API_TOKEN", "")
