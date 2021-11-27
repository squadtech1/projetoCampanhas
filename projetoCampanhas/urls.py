from django.contrib import admin
from django.urls import include, path
from .views import home, listaCampanhas


urlpatterns = [
    path('', home),
    path('home/', home, name='home'),
    path('lista/', listaCampanhas, name='lista'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('campanha/', include("campanha.urls")),
]
