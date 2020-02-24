end = 0

from flask import render_template
from flask_classful import route
from flask_login import login_required

from .view import View

class ItemsView(View):
    @route("", methods=["GET"])
    @login_required
    def index(self):
        return render_template("items/index.html")
    end
end
