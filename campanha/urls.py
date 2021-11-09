from django.urls import path
from .views import criarCampanha
from .views import fazerDoacao
from .views import gerenciaCampanha
# from .views import form_campanha


urlpatterns = [
    path('criacao/', criarCampanha, name='criar'),
    path('doacao/', fazerDoacao, name='doar'),
    path('gerencia-campanha/', gerenciaCampanha, name='gerenciar'),
    # path('form-campanha/', form_campanha, name='form-campanha')
]
