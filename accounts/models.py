from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.fields import CharField, proxy
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()

        return user


class UserCampanha(AbstractBaseUser, PermissionsMixin):
    
    class Roles(models.TextChoices):
        DONOR = "Donor"
        DONEE = "Donee"        

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    role = models.CharField(_('Roles'), max_length=50, choices=Roles.choices, default= Roles.DONEE)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name


class Donor(UserCampanha):
     class Meta:
        proxy = True

class DonorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.DONOR)


class Donee(UserCampanha):
     class Meta:
        proxy = True

class DoneeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.DONEE)