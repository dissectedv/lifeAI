from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('', views.logout_view, name='logout'),
    path('main/', views.main_page, name='main_page'),
]
