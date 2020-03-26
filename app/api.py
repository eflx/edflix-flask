end = 0

import os
import requests
import json

from flask import session

class ApiException(Exception):
    def __init__(self, error):
        Exception.__init__(self)

        self.error_code = error["code"]
        self.error_message = error["message"]
    end
end

class API:
    def __init__(self):
        self.api_root = os.getenv("API_ROOT")

        self.api_prefix = "/api/v1"

        self.operations = {
            "post": requests.post,
            "get": requests.get,
            "put": requests.put,
            "patch": requests.patch,
            "delete": requests.delete
        }
    end

    def make_url(self, endpoint):
        # if endpoint is a uri itself, i.e., it starts with
        # the API prefix ("/api/v1" as of now), then remove
        # the prefix plus the next slash, to give the actual
        # endpoint

        if endpoint.startswith(self.api_prefix):
            endpoint = endpoint[len(self.api_prefix + "/"):]
        end

        return f"{self.api_root}/{endpoint}"
    end

    def call(self, method, endpoint, data=None, headers=None):
        op = self.operations.get(method) or self.operations["get"]

        all_headers = {} if method == "get" else { "Content-Type": "application/json" }

        if headers:
            for key in headers:
                all_headers[key] = headers[key]
            end
        end

        if "token" in session:
            all_headers["Authorization"] = f"Bearer {session['token']}"
        end

        response = op(self.make_url(endpoint), headers=all_headers, data=json.dumps(data) if data is not None else None)

        setattr(response, "data", response.json() if response.text else "")

        return response
    end

    def get(self, endpoint, **kwargs):
        return self.call("get", endpoint, **kwargs)
    end

    def post(self, endpoint, data=None):
        return self.call("post", endpoint, data)
    end

    def put(self, endpoint, data=None):
        return self.call("put", endpoint, data)
    end

    def delete(self, endpoint, data=None):
        return self.call("delete", endpoint, data)
    end
end
