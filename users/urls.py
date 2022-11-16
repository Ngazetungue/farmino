from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from .views import RegisterPageView

urlpatterns = [
     path("", LoginView.as_view(), name="login"),
    path("register/", RegisterPageView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
