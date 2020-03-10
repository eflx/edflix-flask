end = 0

from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

from app.forms import Form

class ForgotPasswordForm(Form):
    email = EmailField("Email",
        validators=[
            DataRequired(message="Email is required"),
            Email("Email address must be of the form user@host")
        ]
    )
end
