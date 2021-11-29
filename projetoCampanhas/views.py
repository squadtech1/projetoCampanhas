from django.shortcuts import render
from accounts.models import User
from campanha.models import Campanha


def home(request):
    return render(request, 'home.html')


def listaCampanhas(request):
    user = request.user
    campanhas = Campanha.objects.filter(donor_id=user.id)
    context = {
        'campanhas': campanhas
    }
    return render(request, 'lista-campanhas.html', context=context)

def listaBeneficiados(request):
    beneficiados = User.objects.filter(role=User.Roles.DONEE)
    print(beneficiados[0])
    context = {
        'beneficiados': beneficiados
    }
    return render(request, 'lista-beneficiados.html', context=context)
