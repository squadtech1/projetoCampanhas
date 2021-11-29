from django.contrib import admin
from django.urls import include, path
from .views import *

app_name = 'campanha'
urlpatterns = [
    path('', home),
    path('home/', home, name='home'),
    path('minhas-campanhas/', listaCampanhas, name='minhas-campanhas'),
    path('lista-beneficiados/', listaBeneficiados, name='lista-beneficiados'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('campanha/', include("campanha.urls")),
]
