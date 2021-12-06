from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from accounts.models import User
from .models import Campanha, DonationItem
from django.utils.timezone import now

class CampanhaForm(forms.Form):

    name = forms.CharField(
        label="Nome"
        )

    start = forms.DateField(
        initial=now,
        label="Começo",
        widget=forms.DateInput(attrs={'type': 'date'})
        )

    end = forms.DateField(
        label="Fim",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    description = forms.CharField(
        max_length=50,
        label='Descrição',
        widget=forms.Textarea(attrs={'type': 'textarea'})
        )

    donee = forms.ModelChoiceField(
        queryset=User.objects.filter(role="Beneficiário").order_by("username"),
        label="Beneficiado"
        )
    item = forms.CharField(max_length=50)



    volume = forms.IntegerField(label='Quantidade')
    
    name.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white', 'placeholder':'Dê um título para sua Campanha'})
    start.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})
    end.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})
    description.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white','rows':'3', 'cols':'50', 'placeholder': 'Um resumo da campanha e seus objetivos'})
    donee.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})
    item.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white', 'placeholder':'Escreva qual o ITEM da Doação'})
    volume.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white', 'placeholder':'Qual a QUANTIDADE que deseja doar?'})

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationItem
        fields = '__all__'

class DoneeNeedForm(forms.Form):

    need = forms.CharField(
        label="Atual Necessidade",
        widget=forms.Textarea(attrs={'type': 'textarea'})
        )
    need.widget.attrs.update({'class':'u-grey-10 u-input u-input-rectangle','rows':'3', 'cols':'50', 'placeholder': 'Em resumo, descreva o que você mais precisa'})

class PostForm(forms.Form):

    post = forms.CharField(
        label="Escreva Aqui",
        )
    post.widget.attrs.update({'class':'u-grey-10 u-input u-input-rectangle','rows':'3', 'cols':'50', 'placeholder': 'O que você quer dizer para o mundo?'})