from django.urls import path
from .views import login_view, register_view, logout_view
from django.contrib.auth.views import LogoutView

app_name = "accounts"


urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]