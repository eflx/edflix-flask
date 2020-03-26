end = 0

from app import api
from app.api import ApiException

from .model import Model

class Collection(Model):
    def __init__(self, **params):
        Model.__init__(self, **params)
    end

    @staticmethod
    def all():
        response = api.get("collections")

        if not response.ok:
            raise ApiException(response.data)
        end

        return list(map(lambda data: Collection(**data), response.data["collections"]))
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

    @staticmethod
    def get(id):
        response = api.get(f"collections/{id}")

        if not response.ok:
            raise ApiException(response.data)
        end

        return Collection(**response.data)
    end

    def save(self):
        response = api.put(self.url, data={
            "title": self.title
        })

        if not response.ok:
            raise ApiException(response.data)
        end

        return self
    end

    def delete(self):
        response = api.delete(self.url)

        if not response.ok:
            raise ApiException(response.data)
        end
    end

    def __repr__(self):
        return f"Collection '{self.title}'"
    end
end
