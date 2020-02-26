end = 0

from flask import url_for, redirect
from flask import render_template, flash
from flask import request, session

from werkzeug.urls import url_parse

from flask_classful import route

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from app.forms import SignupForm
from app.forms import LoginForm

from app.tasks import send_verification_email

from app.models import User

from app import api

from .view import View

class UsersView(View):
    @route("/signup/<role>",  methods=["GET", "POST"])
    def signup(self, role):
        if current_user.is_authenticated:
            return redirect("ItemsView:index")
        end

        if not role in ["teacher", "school-admin"]: # get these from the API?
            flash(f"Unknown role '{role}' -- must be one of 'teacher' or 'school-admin'", category="error")

            return redirect(url_for("HomeView:index"))
        end

        signup_form = SignupForm(role)

        if signup_form.validate_on_submit():
            response = api.post(f"users", data=signup_form.data)

            if response.ok:
                send_verification_email(response.data["email"], response.data["token"])
                # flash(f"Please complete your registration by clicking on the verification link in your email.")
                #token = response.json()["token"]

                #flash(f"Please click {url_for('UsersView:verify', token=token, _external=True)} to verify your account")
                flash(f"Please complete your registration by clicking on the verification link in your email {response.data['email']}.")
            else:
                flash(response.json()["message"], category="error")
            end

            return redirect(url_for("UsersView:login"))
        end

        return render_template("users/signup.html", form=signup_form)
    end

    @route("/verify/<token>")
    def verify(self, token):
        response = api.post(f"users/verify", data={ "token": token })

        if not response.ok:
            return render_template("users/verify.html", message=message, ok=response.ok)
        end

        flash(f"User {response.json()['email']} verified successfully")

        return redirect(url_for("UsersView:login"))
    end

    @route("/login", methods=["GET", "POST"])
    def login(self):
        if current_user.is_authenticated:
            return redirect(url_for("ItemsView:index"))
        end

        login_form = LoginForm()

        if login_form.validate_on_submit():
            response = api.post(f"auth/token", data=login_form.data)

            if not response.ok:
                flash(response.json()["message"], category="error")

                # go back to the login page
                return render_template("users/login.html", form=login_form)
            end

            session["token"] = token = response.json()["token"]

            user = User.new(token)

            login_user(user, remember=login_form.remember_me.data)

            next_page = request.args.get("next")

            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("ItemsView:index")
            end

            return redirect(next_page)

            # if not user.verified:
            #     flash("Please verify your email before logging in", category="error")

            #     return redirect(url_for("UsersView:login"))
            # end
        end

        return render_template("users/login.html", form=login_form)
    end

    @route("/logout")
    @login_required
    def logout(self):
        logout_user()

        del session["token"]

        return redirect(url_for("HomeView:index"))
    end

    @route("/profile", methods=["GET"])
    @login_required
    def profile(self):
        pass
    end
end
