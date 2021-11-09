from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CampanhaForm, DonationForm


@login_required
def criarCampanha(request):
    form = CampanhaForm()
    context = {
        'form': form
    }
    return render(request, 'campanha-main.html', context=context)


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
    return render(request, 'campanha-main.html', context=context)
