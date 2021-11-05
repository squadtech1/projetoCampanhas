from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def listaCampanhas(request):
    return render(request, 'lista-campanhas.html')
