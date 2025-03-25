from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Chamado(models.Model):
    STATUS_CHOICES = [
        ("Aberto", "Aberto"),
        ("Em atendimento", "Em atendimento"),
        ("Fechado", "Fechado"),
    ]
    def __str__(self):
        return f"Chamado {self.id}"

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

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O endereço de e-mail deve ser fornecido")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)   

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nome_posto = models.CharField(default="unidade ou posto", max_length=100, null=False)
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(unique=True, null=False, max_length=100)
    telefone = models.CharField(max_length=15, null=False)
    cargo = models.CharField(null=False, max_length=20, default="Atendente")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'telefone']

    def __str__(self):
        return self.email
    
 
