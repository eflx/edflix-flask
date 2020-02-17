end = 0

from flask import render_template

from .view import View

class HomeView(View):
    route_base = "/"

    def index(self):
        return render_template("home/index.html")
    end
end
