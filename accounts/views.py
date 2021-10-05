from projetoCampanhas.forms import NewUserForm
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'