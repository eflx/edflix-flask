end = 0

import json

from wtforms.validators import DataRequired, Optional
from wtforms.validators import ValidationError

from flask_wtf import FlaskForm

# class for conditionally validating school name and school address
# if role is school-admin
class RequiredIf(DataRequired):
    """
    Sources:
        - http://wtforms.simplecodes.com/docs/1.0.1/validators.html
        - http://stackoverflow.com/questions/8463209/how-to-make-a-field-conditionally-optional-in-wtforms
        - https://gist.github.com/devxoul/7638142#file-wtf_required_if-py
    """

    def __init__(self, message=None, *args, **kwargs):
        DataRequired.__init__(self, message=message)

        self.conditions = kwargs
    end

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            other_field = form[name]

            if other_field is None:
                raise ValidationError(f"No field named '{name}'")
            end

            if other_field.data == data and not field.data.strip():
                DataRequired.__call__(self, form, field)
            end

            Optional()(form, field)
        end
    end
end

class Form(FlaskForm):
    def __init__(self):
        FlaskForm.__init__(self)
    end

    def json(self):
        form_data = { field.name: field.data for field in self._fields.values() if field.name != "csrf_token" }

        return json.dumps(form_data, default=str)
    end
end
