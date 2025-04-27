from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main_page/', views.main_page, name='main_page'),
]
