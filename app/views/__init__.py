end = 0

from .view import View

from .home_view import HomeView
from .users_view import UsersView

def initialize(app):
    HomeView.register(app, base_class=View)
    UsersView.register(app, base_class=View)
end
