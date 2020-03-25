end = 0

from wtforms.fields import Field
from wtforms.widgets import TextInput

class ListField(Field):
    """
    Source:
        - https://wtforms.readthedocs.io/en/stable/fields.html#custom-fields
    """

    widget = TextInput()

    def __init__(self, label, **kwargs):
        Field.__init__(self, label, **kwargs)
    end

    def _value(self):
        return ", ".join(self.data) if self.data else ""
    end

    def process_formdata(self, values):
        self.data = [x.strip() for x in values[0].split(',')] if values else []
    end
end
