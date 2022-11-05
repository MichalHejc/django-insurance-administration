from django.urls import path, include

from . import views


app_name = "clients"
urlpatterns = [
    path("", views.index, name="index"),
    path("pojistenci/", views.list_all_clients, name="list-all-clients"),
    path("pojistenci/<int:pk>/", views.client_detail, name="client-detail"),
    path("pojistenci/novy/", views.client_create, name="client-create"),
    path("pojistenci/<int:pk>/upravit/", views.edit_client, name="edit-client"),
    path("pojistenci/<int:pk>/smazat/", views.delete_client, name="delete-client"),
]