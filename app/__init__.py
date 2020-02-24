end = 0

import os

from flask import Flask
from flask_login import LoginManager

login = LoginManager()

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
end

def initialize_views(app):
    from app import views

    views.initialize(app)
end
