import os
from dotenv import load_dotenv
load_dotenv()

login_email = os.getenv("LOGIN_EMAIL")
login_passw = os.getenv("LOGIN_PASS")