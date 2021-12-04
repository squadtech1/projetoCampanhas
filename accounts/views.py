from accounts.models import User
from .forms import UserCreationForm, UserSettings
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import forms

class PasswordsChangeView(PasswordChangeView):
    form_class = forms.PasswordChangeForm
    success_url = reverse_lazy('painel')
    template_name = 'registration/changePassword.html'

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/register.html'


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

    
    


