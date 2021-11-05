from django.urls import path
from .views import criarCampanha
from .views import fazerDoacao
from .views import gerenciaCampanha


urlpatterns = [
    path('criacao/', criarCampanha, name='criar'),
    path('doacao/', fazerDoacao, name='doar'),
    path('gerencia-campanha/', gerenciaCampanha, name='gerenciar')
]
