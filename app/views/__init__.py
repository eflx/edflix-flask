end = 0

from .view import View

from .home_view import HomeView
from .signup_view import SignupView

def initialize(app):
    HomeView.register(app, base_class=View)
    SignupView.register(app, base_class=View)
end
