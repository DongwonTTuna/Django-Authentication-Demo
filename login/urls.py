from .views import *
from django.urls import path


urlpatterns = [
    path("", LoginIDView.as_view(), name="loginid"),
    path("l2", LoginPWView.as_view(), name="loginpw"),
    path('signup', RegisterView.as_view(), name="register")
]