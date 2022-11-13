from django.urls import path

from .views import *


urlpatterns = [
    path("", RatesView.as_view(), name="rates_view"),
]
