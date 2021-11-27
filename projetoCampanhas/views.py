from django.shortcuts import render
from campanha.models import Campanha


def home(request):
    return render(request, 'home.html')


def listaCampanhas(request):
    campanhas = Campanha.objects.all()
    #donationItem = campanha.donationItem.all()
    #print(donationItem)
    context = {
        'campanhas': campanhas
    }
    return render(request, 'lista-campanhas.html', context=context)
