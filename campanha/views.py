from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from campanha.models import Campanha, DonationItem, DoneeNeed, Post
from .forms import CampanhaForm, DonationForm, DoneeNeedForm, PostForm
from accounts.models import User
from datetime import datetime


@login_required
def criarCampanha(request):
    form = CampanhaForm()
    beneficiados = User.objects.filter(role=User.Roles.DONEE)
    print(beneficiados)
    context = {
            'form': form,
            'beneficiados':beneficiados
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
                status = Campanha.Status.PENDING_DONEE_CONFIRMATION, 
                donor = request.user, 
                donee = form.cleaned_data["donee"])
            currentCampanha.save()

            donationItem = DonationItem(
                item = form.cleaned_data["item"], 
                volume = form.cleaned_data["volume"],
                campanha = currentCampanha)
            donationItem.save()
            return redirect('minhas-campanhas')

        return render(request, 'criar-campanha.html', context=context)

@login_required
def editarCampanha(request, id):
    campanha = get_object_or_404(Campanha, pk=id)
    print(campanha.start)
    donationItem = get_object_or_404(DonationItem, campanha_id=campanha.id)
    initial = {'name':campanha.name, 'start':campanha.start, 'end':campanha.end, 'description':campanha.description, 'status':campanha.status, 'donee':campanha.donee, 'item':donationItem.item, 'volume':donationItem.volume}
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
                status = campanha.status, 
                donor = request.user, 
                donee = form.cleaned_data["donee"])
            campanha.save()

            donationItem = DonationItem(
                id = donationItem.id,
                item = form.cleaned_data["item"], 
                volume = form.cleaned_data["volume"],
                campanha = campanha)
            donationItem.save()
            
            return redirect('minhas-campanhas')
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
def doneeDecision(request, id, bool):
    campanha = get_object_or_404(Campanha, pk=id)
    if(bool == 1):
         campanha = Campanha(
                id = campanha.id,
                name = campanha.name, 
                start = campanha.start, 
                end = campanha.end, 
                description = campanha.description, 
                status = Campanha.Status.ENABLED,
                donor = campanha.donor, 
                donee = campanha.donee
             )
         campanha.save()
    else:
        campanha = Campanha(
                id = campanha.id,
                name = campanha.name, 
                start = campanha.start, 
                end = campanha.end, 
                description = campanha.description, 
                status = Campanha.Status.DISABLED,
                donor = campanha.donor.id, 
                donee = campanha.donee.id
             )
        campanha.save()
 
    return redirect('doacoes-recebidas')

@login_required
def criarAtualNecessidade(request):
    form = DoneeNeedForm()
    context = {
            'form': form
        }

    if request.method == "GET":   
        return render(request, 'atual-necessidade.html', context=context)
    else:
        form = DoneeNeedForm(request.POST)
        if form.is_valid():

            try:
                atualNecessidadeBD = get_object_or_404(DoneeNeed, donee_id=request.user.id)
            
                atualNecessidade = DoneeNeed(
                    id = atualNecessidadeBD.id,
                    need = form.cleaned_data["need"],
                    donee = request.user
                    )
                atualNecessidade.save()

                return redirect('home')

            except:
                atualNecessidade = DoneeNeed(
                    need = form.cleaned_data["need"],
                    donee = request.user
                )
                atualNecessidade.save()

                return redirect('home')

        return render(request, 'atual-necessidade.html', context=context)


@login_required
def criarPost(request):

    form = PostForm()
    context = {
            'form': form
        }

    if request.method == "GET":   
        return render(request, 'new-post.html', context=context)
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                    post = form.cleaned_data["post"],
                    user = request.user
                )
            post.save()

            return redirect('home')

        return render(request, 'new-post.html', context=context)

@login_required
def deletarPost(request, id):
	publicacao = get_object_or_404(Post, pk=id)

	if request.method == 'POST':
		publicacao.delete()
		return redirect('painel')


@login_required
def listaUserPosts(request):
    posts = Post.objects.filter(user_id=request.user.id)
    context = {
        "posts": posts
    }

    return render(request, "lista-user-posts.html", context=context)


#ver onde ficará essa view
@login_required
def listarPostagens(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return
    
    

## METODOS ABAIXO NÃO ESTOU SENDO USADOS ##
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
