end = 0

from .view import View

from .home_view import HomeView
from .users_view import UsersView
from .items_view import ItemsView

def initialize(app):
    HomeView.register(app, base_class=View)
    UsersView.register(app, base_class=View)
    ItemsView.register(app, base_class=View)
end
