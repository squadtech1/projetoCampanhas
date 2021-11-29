from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from accounts.models import User
from .models import Campanha, DonationItem
from django.utils.timezone import now

CAMPANHA_STATUS = (
    ("ENABLED", "Enabled"),
    ("DISABLED", "Disabled")
)


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
    
    name.widget.attrs.update({'class':"nameField"})
    start.widget.attrs.update({'class':'startField'})
    end.widget.attrs.update({'class':'endField'})
    description.widget.attrs.update({'class':'descriptionField'})
    #status.widget.attrs.update({'class':'statusField'})
    donee.widget.attrs.update({'class':'doneeField'})
    item.widget.attrs.update({'class':'itemField'})
    volume.widget.attrs.update({'class':'volumeField'})

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationItem
        fields = '__all__'