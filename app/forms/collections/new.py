end = 0

import os

from wtforms import StringField
from wtforms.validators import DataRequired

from app.forms import Form

class NewCollectionForm(Form):
    title = StringField("Title",
        validators=[
            DataRequired(message="Title is required")
        ]
    )
end
