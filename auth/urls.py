from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('accounts/register/', views.SignUp.as_view(), name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
]