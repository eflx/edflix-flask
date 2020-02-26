end = 0

import os
import time

from app import mail

from flask import render_template
from flask import current_app

from flask_mail import Message

# convert to a Celery task later if necessary
def send_email(email, subject, text_body, html_body):
    message = Message(subject, sender=os.getenv("MAIL_DEFAULT_SENDER"), recipients=[user.email])
    message.body = render_template(text_template, user=user, token=token)
    message.html = render_template(html_template, user=user, token=token)

    with current_app.app_context():
        mail.send(message)
    end
end

def send_verification_email(email, token):
    send_email(user, user.get_verification_token(), "[setschoolmw] Verify your email", "users/verify-email.txt", "users/verify-email.html")
end

# def send_password_reset_email(user):
#     send_email(user, "[setschoolmw] Reset your password", "users/reset-password-email.txt", "users/reset-password-email.html")
# end
