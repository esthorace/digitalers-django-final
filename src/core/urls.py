from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import Register, index

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", Register.as_view(template_name="core/register.html"), name="register"),
]
