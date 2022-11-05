from django import forms

from . models import Client


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "surname", "street_address", "city", "postal_code", "email", "phone_number"]