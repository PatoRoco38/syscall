from django.urls import path

from .views import index, abrir_chamado, login_view, relatorio, trocar_senha, logout_view, cadastro
from . import views


urlpatterns = [
    path('', login_view, name='login'),
    path('index/', views.index, name='index'),
    path('abrir_chamado/', views.abrir_chamado, name='abrir_chamado'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('trocar_senha/', views.trocar_senha, name='trocar_senha'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),

]