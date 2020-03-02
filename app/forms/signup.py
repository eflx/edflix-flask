end = 0

import os

from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length, Optional
from wtforms.validators import ValidationError

from .form import Form
from .form import RequiredIf

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

    email = EmailField("Email",
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

    subjects = TextAreaField("Subjects")

    school_name = StringField("School name",
        validators=[
            RequiredIf(role="school-admin", message="School name is required")
        ]
    )

    school_address = TextAreaField("School address",
        validators=[
            RequiredIf(role="school-admin", message="School address is required")
        ]
    )

    application_id = HiddenField("Application id", default=os.getenv("APPLICATION_ID"))

    def __init__(self, role):
        Form.__init__(self)

        self.role.data = role
    end
end
