from django.contrib import admin
from django.urls import include, path
from .views import *

app_name = 'campanha'
urlpatterns = [
    path('', home),
    path('home/', home, name='home'),
    path('minhas-campanhas/', listaCampanhas, name='minhas-campanhas'),
    path('doacoes-recebidas/', doacoesRecebidas, name='doacoes-recebidas'),
    path('lista-beneficiados/', listaBeneficiados, name='lista-beneficiados'),
    path('saiba-mais', saibaMais, name="saiba-mais"),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('campanha/', include("campanha.urls")),
]
