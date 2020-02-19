end = 0

import os

from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length
from wtforms.validators import ValidationError

from .form import Form

class SignupForm(Form):
    first_name = StringField("First name",
        validators=[
            DataRequired(message="First name is required")
        ]
    )

    last_name = StringField("Last name",
        validators=[
            DataRequired(message="Last name is required")
        ]
    )

    email = StringField("Email",
        validators=[
            DataRequired(message="Email is required"),
            Email("Email address must be of the form user@host")
        ]
    )

    password = PasswordField("Password",
        validators=[
            DataRequired(message="Password is required"),
            Length(8, 20, message="Password must be between 8 and 20 characters long")
        ]
    )

    role = HiddenField("Role", default="teacher")

    application_id = HiddenField("Application id", default=os.getenv("APPLICATION_ID"))

    subjects = TextAreaField("Subjects")
end
