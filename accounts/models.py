from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    
    class Roles(models.TextChoices):
        DONOR = "Donor"
        DONEE = "Donee"        

    role = models.CharField(_('Roles'), max_length=50, choices=Roles.choices, default= Roles.DONEE)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)