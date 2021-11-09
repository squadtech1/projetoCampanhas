from django import forms
from .models import Campanha, DonationItem


class CampanhaForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = '__all__'


class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationItem
        fields = '__all__'