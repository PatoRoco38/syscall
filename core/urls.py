from django.urls import path

from .views import abrir_chamado, login

urlpatterns = [
    path('', login, name='login'),
    path('abrir_chamado/', abrir_chamado, name='abrir_chamado'),
    
]