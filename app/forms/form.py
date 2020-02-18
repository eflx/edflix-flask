end = 0

from flask_wtf import FlaskForm

import json

class Form(FlaskForm):
    def json(self):
        form_data = { field.name: field.data for field in self._fields.values() if field.name != "csrf_token" }

        return json.dumps(form_data, default=str)
    end
end
