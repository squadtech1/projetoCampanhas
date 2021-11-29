from django.contrib.auth import forms
from django.forms import widgets
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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget.attrs.update({'class': 'roleField'})
        self.fields['entity_type'].widget.attrs.update({'class': 'entityTypeField'})
        self.fields['cpf_cnpj'].widget.attrs.update({'class': 'cpfCnpjField'})
        self.fields['email'].widget.attrs.update({'class': 'emailField'})
        self.fields['street'].widget.attrs.update({'class': 'streetField'})
        self.fields['state'].widget.attrs.update({'class': 'stateField'})
