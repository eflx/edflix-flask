end = 0

from .view import View

from .home_view import HomeView

def initialize(app):
    HomeView.register(app, base_class=View)
end
