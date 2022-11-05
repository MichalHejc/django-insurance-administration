from django.urls import path, include

from . import views


app_name = "clients"
urlpatterns = [
    path("", views.index, name="index"),
    path("pojistenci/", views.list_all_clients, name="list-all-clients"),
    path("pojistenci/<int:pk>/", views.client_detail, name="client-detail"),
    path("pojistenci/novy/", views.create_client, name="create-client"),
    path("pojistenci/<int:pk>/upravit/", views.edit_client, name="edit-client"),
    path("pojistenci/<int:pk>/smazat/", views.delete_client, name="delete-client"),
    path("pojistenci/<int:pk>/pojisteni/<int:id>/", views.insurance_detail, name="insurance-detail"),
    path("pojistenci/<int:pk>/pojisteni/novy", views.create_insurance, name="create-insurance"),
    path("pojistenci/<int:pk>/pojisteni/<int:id>/upravit", views.edit_insurance, name="edit-insurance"),
    path("pojistenci/<int:pk>/pojisteni/<int:id>/smazat", views.delete_insurance, name="delete-insurance"),
]