# encoding = utf-8

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

TIPO_OS = (
    (

    ),
    (

    ),
)

class OS(Model):
    ref_os = CharField(max_length=5, blank=False, unique=True, verbose_name="#OS", help_text="Referência da OS, no formato OSxxx/xxxx, onde xxx é o número e xxxx é o ano")
    criado_por = ForeignKey(User, verbose_name="Criado Por", help_text="Usuário que criou")
    tipo_os = CharField(choices="")
# Tipo OS
# Dt Criação
# Viabilidade/PE
# Prazo
# Prev Entrega
# Produto
# Velocidade
# #IPs
# Cliente
# Usuário Final
# Projeto
# Usuário/Endereço Atendido
# Status
