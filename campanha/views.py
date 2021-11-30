from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from campanha.models import Campanha, DonationItem
from .forms import CampanhaForm, DonationForm


@login_required
def criarCampanha(request):
    form = CampanhaForm()
    context = {
            'form': form
        }

    if request.method == "GET":   
        return render(request, 'criar-campanha.html', context=context)
    else:
        form = CampanhaForm(request.POST)
        if form.is_valid():

            currentCampanha = Campanha(
                name = form.cleaned_data["name"], 
                start = form.cleaned_data["start"], 
                end = form.cleaned_data["end"], 
                description = form.cleaned_data["description"], 
                status = Campanha.Status.ENABLED, 
                donor = request.user, 
                donee = form.cleaned_data["donee"])
            currentCampanha.save()

            donationItem = DonationItem(
                item = form.cleaned_data["item"], 
                volume = form.cleaned_data["volume"],
                campanha = currentCampanha)
            donationItem.save()
            return redirect('home')

        return render(request, 'criar-campanha.html', context=context)

@login_required
def editarCampanha(request, id):
    campanha = get_object_or_404(Campanha, pk=id)
    initial = {'name':campanha.name, 'start':campanha.start, 'end':campanha.end, 'description':campanha.description, 'status':campanha.status, 'donee':campanha.donee}
    form = CampanhaForm(initial=initial)
    if(request.method == 'POST'):
        form = CampanhaForm(request.POST, initial=initial)
        
        if(form.is_valid()):
            campanha = Campanha(
                id = campanha.id,
                name = form.cleaned_data["name"], 
                start = form.cleaned_data["start"], 
                end = form.cleaned_data["end"], 
                description = form.cleaned_data["description"], 
                status = form.cleaned_data["status"], 
                donor = request.user, 
                donee = form.cleaned_data["donee"])

            campanha.save()
            
            return redirect('home')
        else:
            return render(request, 'editar-campanha.html', {'form': form, 'campanha' : campanha})
    elif(request.method == 'GET'):
        return render(request, 'editar-campanha.html', {'form': form, 'campanha' : campanha})

@login_required
def deletarCampanha(request, id):
	campanha = get_object_or_404(Campanha, pk=id)

	if request.method == 'POST':
		campanha.delete()
		return redirect('home')

	context = {'campanha':campanha}
	return render(request, 'deletar-campanha.html', context)

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
