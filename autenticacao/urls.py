from django.urls import path
from . import views

urlpatterns = [
    path('login', views.logar, name='login'),
    path('sair', views.sair, name='sair'),
    path('registro', views.registro, name='registro'),
]