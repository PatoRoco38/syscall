from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Usuario, Chamado
from .forms import LoginForm
from django.utils.timezone import now, timedelta
from django.http import JsonResponse

# Create your views here.

@login_required
def trocar_senha(request):

    sucesso = False # Inicializa a variável

    if not request.user.cargo == 'Suporte':
        messages.error(request, "Você não tem permissão para alterar senhas!")
        return redirect("index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        nova_senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if nova_senha != confirmar_senha:
            messages.error(request, "As senhas digitadas são diferentes")
            return redirect("trocar_senha")
        
        try:
            usuario = Usuario.objects.get(email=email)
            usuario.password = make_password(nova_senha)
            usuario.save()
            sucesso = True # Senha alterada

            update_session_auth_hash(request, usuario) # Necessário para manter o usuário logado após a troca

            return redirect("index")
        except Usuario.DoesNotExist:
            sucesso = False # Usuário não encontrado
            messages.error(request, "Usuário não encontrado")

    return render(request, "trocar_senha.html", {"sucesso": sucesso})

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

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Email já cadastrado!")
            return redirect("cadastro")

        usuario = Usuario(
            nome_posto=nome_posto,
            nome=nome,
            email=email,
            telefone=telefone,
            cargo=cargo,
        )

        usuario.set_password(senha)
        usuario.save()

        messages.success(request, "Usuário cadastrado com sucesso!")

        return redirect("cadastro")
    return render(request, "cadastro.html")

def index(request):
    return render(request, 'index.html')

def abrir_chamado(request):
    if request.method == "POST":
        posto = request.POST.get("posto")
        telefone = request.POST.get("telefone")
        ipv4 = request.POST.get("ipv4")
        solicitante = request.POST.get("solicitante")
        descricao = request.POST.get("descricao")

        # Cria um novo chamado com os dados do formulário
        chamado = Chamado(
            posto = posto,
            telefone = telefone,
            ipv4 = ipv4,
            solicitante = solicitante,
            descricao = descricao
        )
        chamado.save()

        messages.success(request, "Chamado aberto com sucesso!")
        return redirect("abrir_chamado")

    return render(request, 'abrir_chamado.html')

def atendimento_chamados(request):
    chamados = Chamado.objects.all()
    print("Quantidade de chamados:", chamados.count())
    return render(request, 'atendimento_chamados.html', {'chamados': chamados})

def detalhe_chamado(request, chamado_id):
    chamado = Chamado.objects.get(id=chamado_id)
    return render(request, 'detalhe_chamado.html', {'chamado': chamado})

def atualizar_chamado(request, chamado_id):
    chamado = get_object_or_404(Chamado, id=chamado_id)

    # Para me manter na mesma página após a edição do chamado

    if request.method == "POST":
        chamado.status = request.POST.get("status", chamado.status)
        chamado.resposta = request.POST.get("resposta", chamado.resposta)

        if chamado.status == 'Resolvido':
            chamado.responsavel = request.user.nome
        chamado.save()

        messages.success(request, "Chamado atualizado com sucesso!")

        return render(request, "detalhe_chamado.html", {"chamado": chamado})

    return render(request, "atualizar_chamado.html", {"chamado": chamado})

def logout_view(request):
    logout(request)
    return redirect('login')
