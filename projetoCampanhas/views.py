from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from accounts.models import User
from campanha.models import Campanha, DonationItem, DoneeNeed, Post

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

def userProfile(request, id):
    print(id)
    userProfile = get_object_or_404(User, pk=id)
    doneeNeed = DoneeNeed.objects.filter(donee = userProfile.id)
    userPosts = Post.objects.filter(user_id = userProfile.id)
    context = {
        'userProfile': userProfile,
        'doneeNeed': doneeNeed,
        'userPosts': userPosts
    }
    return render(request, 'perfil.html', context=context)

def saibaMais(request):  
    return render(request, "saiba-mais.html")

def contato(request):  
    return render(request, "contato.html")

@login_required
def painel(request):  
    return render(request, "painel.html")
