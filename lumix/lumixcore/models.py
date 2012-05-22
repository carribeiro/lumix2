# encoding=utf-8

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import DateField

TIPO_OS = (
    ('OSs Comerciais', (
            ('Instalação', 'Instalação'),
            ('Bloqueio', 'Bloqueio'),
            ('Cancelamento', 'Cancelamento'),
            ('Mudança de Velocidade', 'Mudança de Velocidade'),
            ('Mudança de Endereço', 'Mudança de Endereço'),
            ('Co-location', 'Co-location'),
            ('Locação de Equipamento', 'Locação de Equipamento'),
            ('Retirada de Equipamento', 'Retirada de Equipamento'),
            ('Serviços Técnicos', 'Serviços Técnicos'),
        )
    ),
    ('OSs de Engenharia', (
            ('Expansão', 'Expansão'),
            ('Infraestrutura', 'Infraestrutura'),
            ('Manutenção', 'Manutenção'),
        )
    ),
)

ETAPA_OS = (
    ('Entrada', ''),
    ('Planejamento', ''),
    ('Execução', ''),
    ('As Built', ''),
    ('Concluída', ''),
    ('Suspensa', ''),
    ('Cancelada', ''),
    ('Aprovação', ''),
)

SITUACAO_OS = (
    ('OK', 'OK'),
    ('PI', 'Pendência Interna'),
    ('PE', 'Pendência Externa'),
)

class TipoDocumento(Model):
    # TODO: Gerar fixtures pra os documentos padrão do sistema: OS, PE, VE, VI, etc.
    tipo_documento = CharField(max_length=4, blank=False, unique=True, verbose_name="Tipo de Documento", help_text="Tipo de documento, identificado por uma abreviatura de 4 letras")
    nome = CharField(max_length=40, blank=False, unique=True, verbose_name="Nome do Documento", help_text="Nome do documento por extenso")
    descricao = TextField(verbose_name="Descrição do Documento", help_text="Descrição do documento")
    mascara = CharField(max_length=14, blank=False, verbose_name="Máscara", help_text="Máscara padrão de formatação")

class Documento(Model):
    ref_doc = CharField(max_length=14, blank=False, unique=True, verbose_name="#DOC", help_text="Referência do documento, no formato TTTTxxxxx/xxxx, onde TTTT é o tipo, xxxxx é o número sequencial e xxxx é o ano")
    tipo_documento = ForeignKey(TipoDocumento, verbose_name="Tipo de Documento")

class Conta(Model):
    nome_conta = CharField(max_length=40, blank=False, unique=True, verbose_name="Nome da Conta", help_text="Nome da Conta por Extenso")

class Produto(Model):
    # TODO: Gerar fixtures para os produtos padrão do sistema: Fibra Apagada, Connect Flex, IP Flex, etc.
    tipo_produto = CharField(max_length=4, blank=False, unique=True, verbose_name="Tipo de Produto", help_text="Tipo de produto, identificado por uma abreviatura de 4 letras")
    nome = CharField(max_length=40, blank=False, unique=True, verbose_name="Nome do Produto", help_text="Nome do produto por extenso")
    descricao = TextField(verbose_name="Descrição do Produto", help_text="Descrição do Produto")

class OS(Model):
    ref_os = CharField(max_length=14, blank=False, unique=True, verbose_name="#OS", help_text="Referência da OS, no formato OSxxx/xxxx, onde xxx é o número e xxxx é o ano")
    #ref_doc = ForeignKey(Documento, related_name) # TODO: verificar o jeito certo de fazer isso, com herança, ou referenciando o documento
    criado_por = ForeignKey(User, related_name='os_criadas', verbose_name="Criado Por", help_text="Usuário que criou a OS")
    data_criacao = DateField(auto_now_add=True, verbose_name="Data de Criação", help_text="Data na qual a OS foi criada")
    tipo_os = CharField(max_length=40, choices=TIPO_OS, verbose_name="Tipo da OS", help_text="Tipo da OS")
    documento_origem = ForeignKey(Documento, related_name='documentos_originados') # TODO: bolar um jeito de limitar a Viabilidade ou PE
    prazo = IntegerField(verbose_name="Prazo de Execução") # TODO: limitar validação de zero a 360 dias
    previsao_entrega = DateField(verbose_name="Previsão de Entrega", help_text="Data na qual a OS deve ser finalizada")
    produto = ForeignKey(Produto, related_name='produtos')
    velocidade = IntegerField(verbose_name="Velocidade", help_text="Velocidade em Mbps, variando de 1 Mbps a 10.000 Mbps (10 GE)") # TODO: limitar validação de zero a 10 Gbps
    num_ips = IntegerField(verbose_name="Número de IPs", help_text="Número de endereços IP alocados para o cliente além do IP externo do roteador") # TODO: não é uma solução completa e talvez não seja aqui o melhor lugar de guardar essa informação
    cliente = ForeignKey(Conta, related_name='clientes')
    usuario_final = ForeignKey(Conta, related_name='usuarios_finais')
    titulo = CharField(max_length=40, blank=False, unique=True, verbose_name="Título da OS", help_text="Nome da OS com os dados essenciais para identificar a mesma")
    descricao = TextField(verbose_name="Descrição do Produto", help_text="Descrição do Produto")
    endereco_atendido = TextField(verbose_name="Endereço Atendido", help_text="Usuário final ou endereço atendido pela OS")
    etapa = CharField(max_length=20, choices=ETAPA_OS, blank=False, verbose_name="Etapa da OS", help_text="Etapa da OS")
    situacao = CharField(max_length=2, choices=SITUACAO_OS, blank=False, verbose_name="Situação da OS", help_text="Situação da OS")
