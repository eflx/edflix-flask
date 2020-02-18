end = 0

import requests

from flask import session
from flask_classful import FlaskView

from lib import api

class View(FlaskView):
    trailing_slash = False

    # def call(self, endpoint, **kwargs):
    #     url = f"{os.getenv('API_URL')}/{endpoint}"

    #     method = kwargs.pop("method", "get").lower()

    #     headers = { "Content-Type": "application/json" } if method in ["post", "put", "delete"] else {}

    #     if method == "get":
    #         response = requests.get(url, params=kwargs)
    #     elif method == "post":
    #         response == requests.post(url, headers=headers, data=kwargs.pop("data") or {})

    #     if method in ["POST", "PUT", "DELETE"]:
    #         op = method
    #     end

    #     # self.logger.info("{method} {url}".format(method=method, url=url))

    #     # only two methods supported currently -- GET and PUT
    #     if method == "GET":
    #         response = requests.get(url, headers=headers, params=kwargs)
    #     elif method == "PUT":
    #         headers["Content-Type"] = "application/json"

    #         response = requests.put(url, headers=headers, json=kwargs.get("body"))
    #     end

    #     if response.status_code == 401: # Unauthorized (needs new access token)
    #         return redirect(url_for("UsersView:login"))
    #     end

    #     if not response.ok:
    #         pass
    #         # self.logger.error("Error {status_code} while calling {url}".format(url=response.url, status_code=response.status_code))
    #         # self.logger.error(response.text)

    #         # log the exception
    #         # raise Exception("Error {status_code} while calling {url}".format(url=response.url, status_code=response.status_code))
    #     end

    #     return response
    # end
end
