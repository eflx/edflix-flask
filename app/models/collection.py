end = 0

from app import api
from app.api import ApiException

from .model import Model

class Collection(Model):
    def __init__(self, **params):
        Model.__init__(self, **params)
    end

    @staticmethod
    def new(title):
        response = api.post(f"collections", data={
            "title": title
        })

        if not response.ok:
            raise ApiException(response.data)
        end

        return Collection(**response.data)
    end

    def __repr__(self):
        return f"Collection '{self.title}'"
    end
end
