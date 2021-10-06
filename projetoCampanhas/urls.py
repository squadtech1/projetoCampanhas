from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include("campanha.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('', include("campanha.urls")),
]
