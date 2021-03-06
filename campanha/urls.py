from django.urls import path
from .views import *
# from .views import form_campanha

app_name = 'campanha'
urlpatterns = [
    path('criacao/', criarCampanha, name='criar'),
    path('editar/<int:id>/', editarCampanha, name='editar'),
    path('deletar/<int:id>/', deletarCampanha, name='deletar'),
    path('doacao/', fazerDoacao, name='doar'),
    path('gerencia-campanha/', gerenciaCampanha, name='gerenciar'),
    path('campanhas/', getCampanhas, name='campanhas'),
    path('donee-decision/<int:id>/<int:bool>', doneeDecision, name = 'donee-decision'),
    path('atual-necessidade/', criarAtualNecessidade, name='atual-necessidade'),
    path("criarPost/", criarPost, name="criarPost"),
    path('deletarPost/<int:id>/', deletarPost, name="deletarPost"),
    path("userPosts", listaUserPosts, name="userPosts"),
    path("listaPosts", listarPostagens, name="listaPosts")
    # path('form-campanha/', form_campanha, name='form-campanha')
]
