from django.contrib import admin
from django.urls import path, include  # Adicione 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lifeAI.urls')),  # Inclui as URLs do app lifeAI
]
