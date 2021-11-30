from accounts.models import User
from .forms import UserCreationForm, UserSettings
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/register.html'


@login_required 
def settings(request):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    form = UserSettings(instance=request.user)
    context = {
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'registration/settings.html', context=context)
    else:
        form = UserSettings(request.POST, instance=request.user)   
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            return render(request, 'registration/settings.html', context=context)
    


