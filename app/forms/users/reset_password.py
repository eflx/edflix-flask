end = 0

from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Length, Email

from app.forms import Form

class ResetPasswordForm(Form):
    email = EmailField("Email",
        validators=[
            DataRequired(message="Email is required"),
            Email(message="Email must be of the form user@host")
        ]
    )

    new_password = PasswordField("New password",
        validators=[
            DataRequired(message="New password is required"),
            Length(8, 20, message="Password must be between 8 and 20 characters long")
        ]
    )

    password_confirmation = PasswordField("Confirm password",
        validators=[
            DataRequired(message="Password verification is required"),
            EqualTo("new_password", message="Passwords must match")
        ]
    )
end
