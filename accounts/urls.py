from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views


app_name = "accounts"
urlpatterns = [
    path('register/', views.SignUp.as_view(), name="register"),
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login')
]