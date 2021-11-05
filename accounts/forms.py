from django.contrib.auth import forms
from .models import User

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        #fields = ["email", "username", "role", "password"]
        #TODO adicionar cpf e cnpj de acordo com o valor do 'role'
        #TODO deixar o campo password 'nao visivel'

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ("role", "entity_type", "cpf_cnpj", "email","street", "state",)

