from django.urls import path, include
from . import views



urlpatterns = [
    path("", views.home_page, name="home"),
    path("api/send-email", views.receive_data_from_fe, name="receive_data_from_fe")
]

