from accounts.models import User
from .forms import UserCreationForm, UserSettings
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import forms
from validate_docbr import CPF, CNPJ
from django.contrib import messages

class PasswordsChangeView(PasswordChangeView):
    form_class = forms.PasswordChangeForm
    success_url = reverse_lazy('painel')
    template_name = 'registration/changePassword.html'

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/register.html'

def register(request):
    cpf = CPF()
    cnpj = CNPJ()
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cpfCnpj = form.cleaned_data["cpf_cnpj"]
            if form.cleaned_data["entity_type"] == User.EntityType.FISICA:
                if cpf.validate(cpfCnpj):
                    form.save()
                    return redirect('accounts:login')
                else:
                    context = {'form': form, 'isCpfCnpjValid':False}
            elif form.cleaned_data["entity_type"] == User.EntityType.JURIDICA: 
                if cnpj.validate(cpfCnpj):
                    form.save()
                    return redirect('accounts:login')
                else:
                    messages.error(request, 'The form is invalid.')
            return render(request, 'registration/register.html', context)

    context = {'form': form, 'isCpfCnpjValid':True}
    return render(request, 'registration/register.html', context)


@login_required 
def settings(request):
    form = UserSettings(instance=request.user)
    user = get_object_or_404(User, pk=request.user.id)
    context = {
        'form': form,
        'user': user
    }
    if request.method == 'GET':
        return render(request, 'registration/settings.html', context=context)
    else:
        form = UserSettings(request.POST, instance=request.user)   
        if form.is_valid():
            form.save()
            return redirect('painel')
        
        else:
            return render(request, 'registration/settings.html', context=context)

@login_required 
def removeAccount(request):
    user = get_object_or_404(User, pk=request.user.id)

    if request.method == "POST":
        user.delete()
        return redirect('home')
    return render(request, 'registration/remove.html')

    
    


