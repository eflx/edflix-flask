end = 0

import os

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from .api import API

login = LoginManager()
mail = Mail()
api = API()

def create_app(config_name="development"):
    from app import models

    app = Flask(__name__)
    app.config.from_object("config.default")
    app.config.from_object(f"config.{config_name}")

    initialize_extensions(app)
    initialize_views(app)

    return app
end

def initialize_extensions(app):
    login.init_app(app)
    login.login_view = "UsersView:login"

    mail.init_app(app)
end

def initialize_views(app):
    from app import views

    views.initialize(app)
end
