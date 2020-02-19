end = 0

import os
import requests as http

from flask import url_for, redirect
from flask import render_template, flash

from flask_classful import route

from app.forms import SignupForm

from .view import View

class SignupView(View):
    @route("/teacher",  methods=["GET", "POST"])
    def index(self):
        signup_form = SignupForm()

        if signup_form.validate_on_submit():
            response = http.post(f"{os.getenv('API_URL')}/users", headers={"Content-Type": "application/json"}, data=signup_form.json())

            if response.ok:
                flash(f"Please complete your registration by clicking on the verification link in your email.")
            else:
                flash(response.json()["message"], category="error")
            end

            return redirect(url_for("HomeView:index"))
        end

        return render_template("signup/index.html", form=signup_form)
    end
end
