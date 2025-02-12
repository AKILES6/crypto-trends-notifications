import os
from dotenv import load_dotenv

load_dotenv()
cg_api_key = os.getenv("CG_API_KEY")
sender_email = os.getenv("SENDER_EMAIL")
gmail_app_pass = os.getenv("GMAIL_APP_PASS")
