end = 0

from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

from app.models import User

from app.forms import Form

class ChangePasswordForm(Form):
    current_password = PasswordField("Password",
        validators=[
            DataRequired(message="Current password is required"),
            Length(8, 20, message="Password must be between 8 and 20 characters long")
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
