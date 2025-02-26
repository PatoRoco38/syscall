from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
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

def relatorio(request):
    return render(request, 'relatorio.html')

def troca_senha(request):
    return render(request, 'troca_senha.html')

def logout_view(request):
    logout(request)
    return redirect('login')
