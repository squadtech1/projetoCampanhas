from django import forms
from django.db import models
from django.db.models import fields

from accounts.models import User
from .models import Campanha, DonationItem
from django.utils.timezone import now

CAMPANHA_STATUS = (
    ("ENABLED", "Enabled"),
    ("DISABLED", "Disabled")
)


class CampanhaForm(forms.Form):
    name = forms.CharField(max_length=50)
    start = forms.DateField(initial=now)
    end = forms.DateField()
    description = forms.CharField(max_length=50)
    status = forms.ChoiceField(choices = CAMPANHA_STATUS)
    donor = forms.ModelChoiceField(queryset=User.objects.all().order_by("username"))
    donee = forms.ModelChoiceField(queryset=User.objects.all().order_by("username"))
    item = forms.CharField(max_length=50)
    volume = forms.IntegerField()
    #campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, null=True, related_name="campanha")


class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationItem
        fields = '__all__'