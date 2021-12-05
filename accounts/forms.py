from django.contrib.auth import forms
from django import forms as form
from django.forms import widgets
from .models import User
from django.db import models
from validate_docbr import CPF, CNPJ
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import requests
import json

ESTADOS = []

class UserSettings(forms.UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email','street', 'state','description']

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ("first_name", "role", "entity_type", "cpf_cnpj", "email","street", "state","description",)
        
    def __init__(self, *args, **kwargs):

        api_url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
        response = requests.get(api_url)
        estadoList = response.json()

        for estado in estadoList:
            ESTADOS.append(estado['nome'])

        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['first_name'].label = "Nome"
        self.fields['role'] = form.ChoiceField(choices=tuple([(name, name) for name in User.Roles]))
        self.fields['role'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['role'].label = "Tipo do Cadastro"
        self.fields['username'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['username'].label = "Nome de Usuário"
        self.fields['entity_type'] = form.ChoiceField(choices=tuple([(name, name) for name in User.EntityType]))
        self.fields['entity_type'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['entity_type'].label = "Pessoa Física ou Jurídica?"
        self.fields['cpf_cnpj'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['cpf_cnpj'].label = "CPF ou CNPJ"
        self.fields['email'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['email'].label = "E-mail"
        self.fields['street'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['street'].label = "Endereço"
        self.fields['state'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['state'].label = "Estado"
        self.fields['state'] = form.ChoiceField(choices=tuple([(estado, estado) for estado in ESTADOS]))
        self.fields['description'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['description'].label = "Descrição"
        self.fields['password1'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})
        self.fields['password2'].widget.attrs.update({'class': 'u-grey-10 u-input u-input-rectangle'})


    def clean(self):
        cpf = CPF()
        cnpj = CNPJ()
        super(UserCreationForm, self).clean()

        cpfCnpj = self.cleaned_data.get("cpf_cnpj")
        entityType = self.cleaned_data.get("entity_type")

        
        if entityType == User.EntityType.FISICA:
            if not cpf.validate(cpfCnpj):
                self.add_error('cpf_cnpj', 'Por favor, insira um CPF válido')
      
        elif entityType == User.EntityType.JURIDICA:
            print(cnpj.validate(cpfCnpj))
            if not cnpj.validate(cpfCnpj):
                self.add_error('cpf_cnpj', 'Por favor, insira um CNPJ válido')
        
        return self.cleaned_data
