from django.db import models

# Create your models here.
class Chamado(models.Model):
    id = models.Model(int, primary_key=True)
    numero = models.Model(str, unique=True, max_length=10, nullable=False)
    posto = models.Model(str, nullable=False, max_length=100)
    telefone = models.Model(str, nullable=False, max_length=15)
    ipv4 = models.Model(str, nullable=False, max_length=15)
    solicitante = models.Model(str, nullable=False, max_length=100)
    status = models.Model(str, nullable=False, default="Aberto")
    acao = models.Model(str, nullable=True, max_length=255)
    resposta = models.Model(str, nullable=True)
    descricao = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(auto_now_add=True)


class Usuario(models.Model):
    id = models.Model(int, primary_key=True)
    nome_posto = models.Model(str, max_length=100, nullable=False)
    nome_usuario = models.Model(str, max_length=100, nullable=False)
    email_unidade = models.Model(str, unique=True, nullable=False)
    telefone = models.Model(str, max_length=15, nullable=False)
    tipo = models.Model(str, nullable=False, max_length=20, default="Cliente")

    def __str__(self):
        return self.descricao
    
