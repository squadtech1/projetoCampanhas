from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from accounts.models import User
from .models import Campanha, DonationItem
from django.utils.timezone import now

'''
CAMPANHA_STATUS = (
    ("ENABLED", "Enabled"),
    ("DISABLED", "Disabled"),
     ("PENDING_DONEE_CONFIRMATION", "Pending Donee Confirmation")
)
'''

class CampanhaForm(forms.Form):

    name = forms.CharField(
        label="Nome"
        )

    start = forms.DateField(
        initial=now,
        label="Começo"
        )

    end = forms.DateField(
        label="Fim"
    )

    description = forms.CharField(
        max_length=50,
        label='Descrição'
        )

    #status = forms.ChoiceField(choices = CAMPANHA_STATUS)

    donee = forms.ModelChoiceField(
        queryset=User.objects.filter(role="Donee").order_by("username"),
        label="Beneficiado"
        )
    item = forms.CharField(max_length=50)



    volume = forms.IntegerField(label='Quantidade')
    
    name.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})
    start.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white', 'type':'date'})
    end.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})
    description.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})
    #status.widget.attrs.update({'class':'statusField'})
    donee.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})
    item.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})
    volume.widget.attrs.update({'class':'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'})

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationItem
        fields = '__all__'

class DoneeNeedForm(forms.Form):

    need = forms.CharField(
        label="Atual Necessidade"
        )
    need.widget.attrs.update({'class':"needField"})

class PostForm(forms.Form):

    post = forms.CharField(
        label="New Post"
        )
    post.widget.attrs.update({'class':"postField"})