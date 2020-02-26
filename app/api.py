end = 0

import os
import requests
import json

from flask import session

class API:
    def __init__(self):
        self.api_root = os.getenv("API_ROOT")

        self.operations = {
            "post": requests.post,
            "get": requests.get,
            "put": requests.put,
            "patch": requests.patch,
            "delete": requests.delete
        }
    end

    def call(self, method, uri, data=None, headers=None):
        op = self.operations.get(method) or self.operations["get"]

        all_headers = {} if method in ["get", "delete"] else { "Content-Type": "application/json" }

        if headers:
            for key in headers:
                all_headers[key] = headers[key]
            end
        end

        if "token" in session:
            all_headers["Authorization"] = f"Bearer {session['token']}"
        end

        response = op(f"{self.api_root}/{uri}", headers=all_headers, data=json.dumps(data) if data is not None else None)

        setattr(response, "data", response.json())

        return response
    end

    def get(self, uri, **kwargs):
        return self.call("get", uri, **kwargs)
    end

    def post(self, uri, data=None):
        return self.call("post", uri, data)
    end

    def put(self, uri, data=None):
        return self.call("put", uri, data)
    end

    def delete(self, uri, data=None):
        return self.call("delete", uri, data)
    end
end
