from django.urls import path, include

from . import views


app_name = "clients"
urlpatterns = [
    path("", views.index, name="index")
]