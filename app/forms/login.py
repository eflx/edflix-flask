end = 0

from flask_wtf import FlaskForm as Form

from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(Form):
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

    remember_me = BooleanField("Remember me")
end
