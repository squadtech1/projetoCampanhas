from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def criarCampanha(request):
    return render(request, "campanha-main.html")


@login_required
def fazerDoacao(request):
    return render(request, 'doacao.html')


@login_required
def gerenciaCampanha(request):
    return render(request, 'gerencia-campanha.html')
