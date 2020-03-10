end = 0

import os
import time

from app import mail

from flask import render_template
from flask import current_app

from flask_mail import Message

# convert to a Celery task later if necessary
def send_email(email, subject, text_body, html_body):
    message = Message(subject, sender=os.getenv("MAIL_DEFAULT_SENDER"), recipients=[email])
    message.body = text_body
    message.html = html_body

    with current_app.app_context():
        mail.send(message)
    end
end

def send_verification_link(email, verification_token):
    text_body = render_template("users/verify-email.txt", email=email, token=verification_token)
    html_body = render_template("users/verify-email.html", email=email, token=verification_token)

    send_email(email, "[eflx] Verify your email", text_body, html_body)
end

def send_verification_confirmation(email):
    text_body = render_template("users/verified-email.txt", email=email)
    html_body = render_template("users/verified-email.html", email=email)

    send_email(email, "[eflx] Email verified", text_body, html_body)
end

def send_password_change_notification(email):
    text_body = render_template("users/password-changed-email.txt", email=email)
    html_body = render_template("users/password-changed-email.html", email=email)

    send_email(email, "[eflx] Your password was changed", text_body, html_body)
end

def send_password_reset_link(email, token):
    text_body = render_template("users/reset-password-email.txt", email=email, token=token)
    html_body = render_template("users/reset-password-email.html", email=email, token=token)

    send_email(email, "[eflx] Reset your password", text_body, html_body)
end
