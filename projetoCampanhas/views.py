from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import User
from campanha.models import Campanha, DonationItem

def home(request):
    return render(request, 'home.html')

@login_required
def listaCampanhas(request):
    user = request.user
    campanhas = Campanha.objects.filter(donor_id=user.id)
    donationItems = DonationItem.objects.all()
    context = {
        'campanhas': campanhas,
        'donationItems': donationItems
    }
    return render(request, 'lista-campanhas.html', context=context)

@login_required
def doacoesRecebidas(request):
    user = request.user
    campanhas = Campanha.objects.filter(donee_id=user.id)
    donationItems = DonationItem.objects.all()
    print(campanhas)
    context = {
        'campanhas': campanhas,
        'donationItems': donationItems
    }
    return render(request, 'doacoes-recebidas.html', context=context)

def listaBeneficiados(request):
    beneficiados = User.objects.filter(role=User.Roles.DONEE)
    context = {
        'beneficiados': beneficiados
    }
    return render(request, 'lista-beneficiados.html', context=context)

def saibaMais(request):  
    return render(request, "saiba-mais.html")

def contato(request):  
    return render(request, "contato.html")

@login_required
def painel(request):  
    return render(request, "painel.html")
