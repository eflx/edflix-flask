end = 0

from flask import render_template, redirect, url_for
from flask_login import current_user

from .view import View

class HomeView(View):
    route_base = "/"

    def index(self):
        if current_user.is_authenticated:
            return redirect(url_for("ItemsView:index"))
        end

        return render_template("home/index.html")
    end
end
