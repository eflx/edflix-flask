end = 0

import os

from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

from app.forms import Form

class ProfileForm(Form):
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

    email = EmailField("Email") # no validations here; this is a readonly field
end
