from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.campanhaView, name="campanhas"),
]