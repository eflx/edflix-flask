end = 0

import os

from flask import Flask

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object("config.default")
    app.config.from_object(f"config.{config_name}")

    initialize_extensions(app)
    initialize_views(app)

    return app
end

def initialize_extensions(app):
    pass
end

def initialize_views(app):
    from app import views

    views.initialize(app)
end
