end = 0

from flask import session
from flask_login import UserMixin

from app import login
from app import api

from .model import Model

@login.user_loader
def load_user(id):
    return User.new(id)
end

class User(UserMixin, Model):
    def __init__(self, **params):
        Model.__init__(self, **params)
    end

    def get_id(self):
        return session.get("token")
    end

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    end

    @staticmethod
    def new(token):
        response = api.get(f"users/userinfo")

        if not response.ok:
            raise Exception(response.json())
        end

        return User(**response.json())
    end

    def __repr__(self):
        return f"User ({self.email})"
    end
end
