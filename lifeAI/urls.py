from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),

    path('home/', views.home_page, name='home_page'),
    path('chatIA/', views.chat_page, name='chatIA'),
    path('configuracoes/', views.config_page, name='configuracoes'),
    path('desempenho/', views.desempenho_page, name='desempenho'),
    path('rotina/', views.rotina_page, name='rotina'),
]
