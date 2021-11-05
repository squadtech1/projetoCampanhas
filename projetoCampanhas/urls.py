from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import home, listaCampanhas


urlpatterns = [
    path('', home),
    path('home/', home, name='home'),
    path('lista/', listaCampanhas, name='lista'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('campanha/', include("campanha.urls"))
]
