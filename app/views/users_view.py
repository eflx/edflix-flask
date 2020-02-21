end = 0

import os
import json
import requests as http

from flask import url_for, redirect
from flask import render_template, flash
from flask import session

from flask_classful import route

from app.forms import SignupForm
from app.forms import LoginForm

from .view import View

class UsersView(View):
    @route("/signup/<role>",  methods=["GET", "POST"])
    def signup(self, role):
        if not role in ["teacher", "school-admin"]: # get these from the API?
            flash(f"Unknown role '{role}' -- must be one of 'teacher' or 'school-admin'", category="error")

            return redirect(url_for("HomeView:index"))
        end

        signup_form = SignupForm(role)

        if signup_form.validate_on_submit():
            response = http.post(f"{os.getenv('API_URL')}/users", headers={"Content-Type": "application/json"}, data=signup_form.json())

            if response.ok:
                # flash(f"Please complete your registration by clicking on the verification link in your email.")
                token = response.json()["token"]

                flash(f"Please click {url_for('UsersView:verify', token=token, _external=True)} to verify your account")
            else:
                flash(response.json()["message"], category="error")
            end

            return redirect(url_for("HomeView:index"))
        end

        return render_template("users/signup.html", form=signup_form)
    end

    @route("/verify/<token>")
    def verify(self, token):
        response = http.post(f"{os.getenv('API_URL')}/users/verify", headers={"Content-Type": "application/json"}, data=json.dumps({ "token": token }))

        if response.ok:
            message = f"User {response.json()['email']} verified successfully"
        else:
            message = response.json()["message"]
        end

        return render_template("users/verify.html", message=message, ok=response.ok)
    end

    @route("/login", methods=["GET", "POST"])
    def login(self):
        if "token" in session:
            return redirect(url_for("HomeView:index"))
        end

        login_form = LoginForm()

        if login_form.validate_on_submit():
            response = http.post(f"{os.getenv('API_URL')}/auth/token", headers={"Content-Type": "application/json"}, data=login_form.json())

            if response.ok:
                session["token"] = response.json()["token"]
            else:
                flash(response.json()["message"], category="error")
            end

            return redirect(url_for("HomeView:index"))

            # if not user.verified:
            #     flash("Please verify your email before logging in", category="error")

            #     return redirect(url_for("UsersView:login"))
            # end

            # login_user(user, remember=login_form.remember_me.data)

            # next_page = request.args.get("next")
            # if not next_page or url_parse(next_page).netloc != "":
            #     next_page = url_for("RegistrationsView:index")
            # end

            # return redirect(next_page)
        end

        return render_template("users/login.html", form=login_form)
    end
end
