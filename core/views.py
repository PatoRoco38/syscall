from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
"""def login(request):
    return render(request, 'login.html')"""

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index") # Redireciona para a página principal
            else:
                messages.error(request, "Email ou senha incorretos!") # Mensagem de erro
        except User.DoesNotExist:
            messages.error(request, "Email não encontrado!")
    return render(request, "login.html")

def index(request):
    return render(request, 'index.html')

def abrir_chamado(request):
    return render(request, 'abrir_chamado.html')


