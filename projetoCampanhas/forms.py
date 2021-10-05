from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserCampanha

class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserCampanha
        fields = ["email", "user_name", "role", "cpf", "cnpj"]