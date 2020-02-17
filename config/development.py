import os

from .default import *

DEBUG = True
DEVELOPMENT = True
TESTING = False

SQLALCHEMY_ECHO = True

MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = int(os.getenv("MAIL_PORT") or 2525)
MAIL_USE_TLS = True if os.getenv("MAIL_USE_TLS") in ["True", "true", "1"] else False
MAIL_USE_SSL = True if os.getenv("MAIL_USE_SSL") in ["True", "true", "1"] else False
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
