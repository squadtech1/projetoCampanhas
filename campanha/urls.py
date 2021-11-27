from django.urls import path
from .views import *
# from .views import form_campanha

app_name = 'campanha'
urlpatterns = [
    path('criacao/', criarCampanha, name='criar'),
    path('doacao/', fazerDoacao, name='doar'),
    path('gerencia-campanha/', gerenciaCampanha, name='gerenciar'),
    path('campanhas/', getCampanhas, name='campanhas')
    # path('form-campanha/', form_campanha, name='form-campanha')
]
