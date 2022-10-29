from django.urls import path

from .views import MarketView
from .views import *


urlpatterns =[path('', MarketView.as_view(),name='marketmain')]