end = 0

import os
import requests as http

from flask import session
from flask_login import UserMixin

from app import login

from .model import Model

@login.user_loader
def load_user(id):
    print("*** loading user from the API ***")
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
        # call the /users/profile API to get the user
        response = http.get(f"{os.getenv('API_URL')}/users/userinfo", headers={ "Authorization": f"Bearer {session['token']}" })

        if not response.ok:
            raise Exception(response.json())
        end

        user_data = response.json()

        return User(**user_data)
        #return User(first_name="Albus", last_name="Dumbledore", email="albus.dumbledore@hogwarts.edu", verified=True)
    end

    def __repr__(self):
        return f"User ({self.email})"
    end
end
