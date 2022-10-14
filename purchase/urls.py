from .views import *
from django.urls import path


urlpatterns = [
    path("", MarketView.as_view(), name="market"),
    path("", LoginIDView.as_view(), name="loginid"),
    path("l2", LoginPWView.as_view(), name="loginpw"),
]
