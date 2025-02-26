from django.urls import path

from .views import index, abrir_chamado, login_view
from . import views


urlpatterns = [
    path('', login_view, name='login'),
    path('index/', views.index, name='index'),
    path('abrir_chamado/', views.abrir_chamado, name='abrir_chamado'),
    
]