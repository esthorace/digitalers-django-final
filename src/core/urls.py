from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import ProfileUpdate, RegisterCreate, index

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", RegisterCreate.as_view(template_name="core/register.html"), name="register"),
    path("profile/", ProfileUpdate.as_view(template_name="core/profile.html"), name="profile"),
]
