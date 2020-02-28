import os

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") or "this-is-a-secret"

MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = int(os.getenv("MAIL_PORT"))
MAIL_USE_TLS = bool(int(os.getenv("MAIL_USE_TLS")))
MAIL_USE_SSL = bool(int(os.getenv("MAIL_USE_SSL")))
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

DEBUG = True
DEVELOPMENT = True
TESTING = False
