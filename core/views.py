from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Usuario
from .forms import LoginForm

# Create your views here.
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = Usuario.objects.get(email=email)
                user = authenticate(request, username=email, password=password)

                if user is not None:
                    login(request, user)
                    return redirect("index") # Redireciona para a página principal
                else:
                    form.add_error(None, "Email ou senha incorretos!") # Mensagem de erro
            except Usuario.DoesNotExist:
                messages.error(request, "Email não encontrado!")

    return render(request, "login.html", {"form": form})

def cadastro(request):
    if request.method == "POST":
        nome_posto = request.POST.get("nome_posto")
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        cargo = request.POST.get("cargo")
        senha = request.POST.get("senha")

        usuario = Usuario(
            nome_posto=nome_posto,
            nome=nome,
            email=email,
            telefone=telefone,
            cargo=cargo,
        )

        usuario.set_password(senha)
        usuario.save()

        return render(request, "cadastro.html", {"success": True})
    return render(request, "cadastro.html")

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
