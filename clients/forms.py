from django import forms

from . models import Client, Insurance


class CreateClientForm(forms.ModelForm):
    """Curstom form for Client instance creation."""
    
    class Meta:
        model = Client
        fields = ["name", "surname", "street_address", "city", "postal_code", "email", "phone_number"]


class CreateInsuranceForm(forms.ModelForm):
    """Curstom form for Insurance instance creation."""

    class Meta:
        model = Insurance
        fields = ["insurance_type", "subject", "amount", "date_from", "date_to"]