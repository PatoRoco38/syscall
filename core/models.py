from django.db import models
from django.utils.timezone import now

# Create your models here.
class Chamado(models.Model):
    STATUS_CHOICES = [
        ("Aberto", "Aberto"),
        ("Em atendimento", "Em atendimento"),
        ("Fechado", "Fechado"),
    ]

    id = models.AutoField(primary_key=True)
    posto = models.CharField(default="Não informado", max_length=100)
    telefone = models.CharField(default="62999999999", null=False, max_length=15)
    ipv4 = models.GenericIPAddressField(default="0.0.0.0", max_length=15)
    solicitante = models.CharField(default="Solicitante", null=False, max_length=100)
    status = models.CharField(choices=STATUS_CHOICES, default="Aberto", max_length=15)
    acao = models.CharField(null=True, max_length=255)
    resposta = models.CharField(null=True, max_length=500)
    descricao = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    def save(self, *args, **kwargs):

        # Se o chamado acaba de ser fechado e não tem data de fechamento, define a data atual
        if self.status == "Fechado" and self.data_fechamento is None:
            self.data_fechamento = now()
        return super().save(*args, **kwargs)


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome_posto = models.CharField(default="unidade ou posto", max_length=100, null=False)
    nome_usuario = models.CharField(max_length=100, null=False)
    email_unidade = models.CharField(unique=True, null=False, max_length=100)
    telefone = models.CharField(max_length=15, null=False)
    tipo = models.CharField(null=False, max_length=20, default="Cliente")

    def __str__(self):
        return self.descricao
    
