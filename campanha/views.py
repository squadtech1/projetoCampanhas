from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def campanhaView(request):
    return render(request, "campanha/campanhaMain.html")
