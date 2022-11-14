from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """Custom form for client creation. Added field 'is_staff', that determines, if new user will have staff rights"""

    is_staff = forms.BooleanField(label="Zaregistrovat se jako administrátor:", required=False)
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "is_staff"]