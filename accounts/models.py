from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    
    class Roles(models.TextChoices):
        DONOR = "Donor"
        DONEE = "Donee"  

    class EntityType(models.TextChoices):
        FISICA = "Fisica"
        JURIDICA = "Juridica"

    role = models.CharField(_('Roles'), max_length=50, choices=Roles.choices, default= Roles.DONEE)
    entity_type = models.CharField(_('EntityType'), max_length = 8, choices = EntityType.choices, default = EntityType.FISICA)
    cpf_cnpj = models.CharField(max_length=14, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.username)
        # return " Name: " + str(self.username) + "Id: " + str(self.id) + " UserType: " + str(self.role)