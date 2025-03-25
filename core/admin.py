from django.contrib import admin
from .models import Chamado, Usuario

admin.site.site_header = 'SysCall - Sistema de Chamados'
admin.site.index_title = 'Bem vindo ao SysCall'
admin.site.site_title = 'SysCall'

# Register your models here.
admin.site.register(Chamado)
admin.site.register(Usuario)
