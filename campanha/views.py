from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from campanha.models import Campanha, DonationItem
from .forms import CampanhaForm, DonationForm


@login_required
def criarCampanha(request):
    if request.method == "GET":
        form = CampanhaForm()
        context = {
            'form': form
        }
        return render(request, 'criar-campanha.html', context=context)
    else:
        form = CampanhaForm(request.POST)
        if form.is_valid():

            currentCampanha = Campanha(
                name = form.cleaned_data["name"], 
                start = form.cleaned_data["start"], 
                end = form.cleaned_data["end"], 
                description = form.cleaned_data["description"], 
                status = form.cleaned_data["status"], 
                donor = request.user, 
                donee = form.cleaned_data["donee"])
            currentCampanha.save()

            donationItem = DonationItem(
                item = form.cleaned_data["item"], 
                volume = form.cleaned_data["volume"],
                campanha = currentCampanha)
            donationItem.save()

            form = CampanhaForm()

        context = {
            'form': form
        }
        return render(request, 'criar-campanha.html', context=context)


@login_required
def fazerDoacao(request):
    form = DonationForm()
    context = {
        'form': form
    }
    return render(request, 'doacao.html', context=context)


@login_required
def gerenciaCampanha(request):
    return render(request, 'gerencia-campanha.html')


@login_required
def form_campanha(request):
    form = CampanhaForm()
    context = {
        'form': form
    }
    return render(request, 'criar-campanha.html', context=context)

def getCampanhas(request):
    campanhas = Campanha.objects.all()
    donationItems = DonationItem.objects.all()
    print(donationItems[0].campanha.id)
    return
