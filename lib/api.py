end = 0

import os
import json
import requests

from flask import url_for, redirect

class API:
    def __init__(self):
        self.url = os.getenv("API_URL")

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

        response = op(f"{os.getenv('API_URL')}/{uri}", headers=all_headers, data=None if data is None else json.dumps(data))

        # if response.status_code == 401: # Unauthorized (needs new access token)
        #     return redirect(url_for("HomeView:index"))
        # end

        setattr(response, "json", json.loads(response.text))

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
