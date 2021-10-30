from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import admin as authAdmin
from django.db import models

from campanha.models import Campanha
from .forms import UserCreationForm, UserChangeForm
from .models import User

admin.site.register(Campanha)

@admin.register(User)
class UserAdmin(authAdmin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = authAdmin.UserAdmin.fieldsets + ((None, {"fields": ("role", "cpf_cnpj", "entity_type", "street", "state")}),)
