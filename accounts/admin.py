from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import admin as authAdmin
from .forms import UserCreationForm, UserSettings
from .models import User

@admin.register(User)
class UserAdmin(authAdmin.UserAdmin):
    form = UserSettings
    add_form = UserCreationForm
    model = User
    fieldsets = authAdmin.UserAdmin.fieldsets + ((None, {"fields": ("role", "cpf_cnpj", "entity_type", "street", "state", "description")}),)
