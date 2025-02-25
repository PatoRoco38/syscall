from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def abrir_chamado(request):
    return render(request, 'abrir_chamado.html')


