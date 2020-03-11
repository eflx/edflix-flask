end = 0

import os

from flask import url_for, redirect
from flask import render_template, flash
from flask import request, session

from werkzeug.urls import url_parse

from flask_classful import route

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from app.forms.users import SignupForm
from app.forms.users import LoginForm
from app.forms.users import ProfileForm
from app.forms.users import ChangePasswordForm
from app.forms.users import ForgotPasswordForm
from app.forms.users import ResetPasswordForm

from app.lib import tasks

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
                tasks.send_verification_link(response.data["email"], response.data["token"])

                flash(f"Please complete your registration by clicking on the verification link in your email")

                return redirect(url_for("UsersView:login"))
            end

            flash(response.data["message"], category="error")
        end

        return render_template("users/signup.html", form=signup_form)
    end

    @route("/verify/<token>")
    def verify(self, token):
        response = api.post(f"users/verify", data={ "token": token, "application_id": os.getenv("APPLICATION_ID") })

        if not response.ok:
            return render_template("users/verify.html", message=message, ok=response.ok)
        end

        tasks.send_verification_confirmation(response.data["email"])

        flash(f"User {response.data['email']} verified successfully")

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
                flash(response.data["message"], category="error")

                # go back to the login page
                return render_template("users/login.html", form=login_form)
            end

            session["token"] = token = response.data["token"]

            user = User.new(token)

            login_user(user, remember=login_form.remember_me.data)

            next_page = request.args.get("next")

            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("ItemsView:index")
            end

            return redirect(next_page)
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

    @route("/profile", methods=["GET", "POST"])
    @login_required
    def profile(self):
        profile_form = ProfileForm()

        if request.method == "GET":
            profile_form.first_name.data = current_user.first_name
            profile_form.last_name.data = current_user.last_name
            profile_form.email.data = current_user.email
        end

        if profile_form.validate_on_submit():
            response = api.put(current_user.url, data=profile_form.data)

            if not response.ok:
                return redirect(url_for("HomeView:index"))
            end

            return redirect(url_for("ItemsView:index"))
        end

        return render_template("users/profile.html", form=profile_form)
    end

    @route("/change-password", methods=["GET", "POST"])
    @login_required
    def change_password(self):
        change_password_form = ChangePasswordForm()

        if change_password_form.validate_on_submit():
            response = api.put(current_user.url, data=change_password_form.data)

            if not response.ok:
                flash(response.data["message"], category="error")

                return render_template("users/change-password.html", form=change_password_form)
            end

            tasks.send_password_change_notification(current_user.email)

            flash("Password changed successfully")

            return redirect(url_for("ItemsView:index"))
        end

        return render_template("users/change-password.html", form=change_password_form)
    end

    @route("/forgot-password", methods=["GET", "POST"])
    def forgot_password(self):
        # can't have forgotten password if already logged in
        if current_user.is_authenticated:
            return redirect(url_for("ItemsView:index"))
        end

        forgot_password_form = ForgotPasswordForm()

        if forgot_password_form.validate_on_submit():
            response = api.post("users/forgot-password", data={
                "email": forgot_password_form.email.data,
                "application_id": os.getenv("APPLICATION_ID")
            })

            if not response.ok:
                flash(response.data["message"], category="error")

                return redirect(url_for("UsersView:login"))
            end

            tasks.send_password_reset_link(response.data["email"], response.data["token"])

            flash(f"A password reset link has been sent to { response.data['email'] }")

            return redirect(url_for("UsersView:login"))
        end

        return render_template("users/forgot-password.html", form=forgot_password_form)
    end

    @route("/reset-password/<token>", methods=["GET", "POST"])
    def reset_password(self, token):
        # can't reset a password if already logged in
        if current_user.is_authenticated:
            return redirect(url_for("ItemsView:index"))
        end

        reset_password_form = ResetPasswordForm()

        if reset_password_form.validate_on_submit():
            response = api.post("users/reset-password", data={
                "token": token,
                "application_id": os.getenv("APPLICATION_ID"),
                "email": reset_password_form.email.data,
                "new_password": reset_password_form.new_password.data
            })

            if not response.ok:
                flash(response.data["message"], category="error")

                return redirect(url_for("UsersView:login"))
            end

            tasks.send_password_change_notification(response.data["email"])

            flash(f"Your password was reset successfully. You can now login with the new password")

            return redirect(url_for("UsersView:login"))
        end

        return render_template("users/reset-password.html", form=reset_password_form)
    end
end
