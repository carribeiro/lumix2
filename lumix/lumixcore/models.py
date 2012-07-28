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
            ('Mudança de Serviço', 'Mudança de Serviço'),  # Upgrade ou downgrade
            ('Mudança de Endereço', 'Mudança de Endereço'),
            ('Locação de Equipamento', 'Locação de Equipamento'),
            ('Retirada de Equipamento', 'Retirada de Equipamento'),
            ('Serviços Técnicos', 'Serviços Técnicos'),
            ('Bloqueio', 'Bloqueio'),
            ('Cancelamento', 'Cancelamento'),
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


class ERRO_SEQUENCIA_DOC(Exception):
    """ Ocorre se houver uma tentativa de salvar um número de documento fora da sequência """
    pass

class ERRO_ANO_FORA_DE_FAIXA(Exception):
    """ Lumix só aceita documentos internos datados de 2010 até 2019 """
    pass

class TipoDocumento(Model):
    # TODO: Gerar fixtures pra os documentos padrão do sistema: OS, PE, VE, VI, etc.
    # Obs: Cada documento padrão tem uma classe própria
    tipo_doc = CharField(primary_key=True, max_length=4, blank=False, unique=True, verbose_name="Tipo de Documento", help_text="Tipo de documento, identificado por uma abreviatura de 4 letras")
    nome = CharField(max_length=40, blank=False, unique=True, verbose_name="Nome do Documento", help_text="Nome do documento por extenso")
    descricao = TextField(verbose_name="Descrição do Documento", help_text="Descrição do documento")
    mascara = CharField(max_length=14, blank=False, verbose_name="Máscara", help_text="Máscara padrão de formatação")
    classe = CharField(max_length=10, blank=False, unique=True, verbose_name="Nome da Classe", help_text="Nome da Classe que implementa o documento")
    # HACK! Típica de ERPs e sistemas de controle. A alternativa é criar
    # um monte de tabelas adicionais, uma para cada ano. Seria uma
    # solução geral mas muito menos eficiente em termos de armazenamento
    # e pesquisa.
    seq_2010 = IntegerField(default=0)
    seq_2011 = IntegerField(default=0)
    seq_2012 = IntegerField(default=0)
    seq_2013 = IntegerField(default=0)
    seq_2014 = IntegerField(default=0)
    seq_2015 = IntegerField(default=0)
    seq_2016 = IntegerField(default=0)
    seq_2017 = IntegerField(default=0)
    seq_2018 = IntegerField(default=0)
    seq_2019 = IntegerField(default=0)

    def proximo_seq_ano(self, ano):
        try:
            return getattr(self, 'seq_%d' % ano) + 1
        except:
            raise ERRO_ANO_FORA_DE_FAIXA

    def incrementa_seq_ano(self, ano, seq):
        try:
            seq_atual = getattr(self, 'seq_%d' % ano)
            if seq_atual == (seq-1):
            else:
                raise ERRO_SEQUENCIA_DOC
        except:
            raise ERRO_ANO_FORA_DE_FAIXA

from collections import namedtuple
TIPO_DOCUMENTO = namedtuple('TIPO_DOCUMENTO', ('tipo_doc', 'nome', 'descricao', 'mascara', 'classe'))
TIPOS_DOCUMENTO = {
    'OS': TIPO_DOCUMENTO('OS', 'Ordem de Serviço', '', 'OS####/yyyy', 'DocOS'),
    'PE': TIPO_DOCUMENTO('OS', 'Ordem de Serviço', '', 'OS####/yyyy', 'DocOS'),
    'EV': TIPO_DOCUMENTO('OS', 'Ordem de Serviço', '', 'OS####/yyyy', 'DocOS'),
    'OE': TIPO_DOCUMENTO('OS', 'Ordem de Serviço', '', 'OS####/yyyy', 'DocOS'),
    'OCLM': TIPO_DOCUMENTO('OS', 'Ordem de Compra de Last Mile', '', 'OS####/yyyy', 'DocOS'),
}

class Documento(Model):
    # cada documento tem um ID próprio, que é composto do tipo do documento, mais um número sequencial e o ano ao qual se refere

    tipo_documento = ForeignKey(TipoDocumento, verbose_name="Tipo de Documento")
    ref_doc_index = CharField(max_length=14, blank=False, unique=True, verbose_name="#DOC", db_index=True,
                        help_text="Referência do documento, no formato TTTTyyyy/#####, onde TTTT é o tipo, yyyy é o ano e ##### é o número sequencial")

    def ref_doc():
        """ Retorna a referência ao documento em um formato de visualização.
            São as mesmas informações do ref_doc_index, formatadas para
            melhorar a leitura de uma forma mais natural.

            Formato: TT(TT)yyyy/#####
            - TTTT: tipo, com no mínimo duas letras, até quatro (não é largura fixa)
            - yyyy é o ano e ##### é o número sequencial
        """
        pass

    def detalhe(self):
        """ o campo detalhe retornar o detalhamento do documento, de forma 
            polimórfica, para cada tipo de documento, usando o campo 'classe'
            para selecionar a mesma. 

            Isso é necessário porque no Django, a seleção de um documento na 
            classe ancestral de um modelo baseado em 'multi table inheritance'
            não é capaz de selecionar instâncias dos modelos herdeiros.
            Se a query for feita na classe 'pai', somente objetos com a classe
            pai serão retornados.
        """
        pass

class Conta(Model):
    nome_conta = CharField(max_length=40, blank=False, unique=True, verbose_name="Nome da Conta", help_text="Nome da Conta por Extenso")

class Produto(Model):
    # TODO: Gerar fixtures para os produtos padrão do sistema: Fibra Apagada, Connect Flex, IP Flex, etc.
    tipo_produto = CharField(max_length=4, blank=False, unique=True, verbose_name="Tipo de Produto", help_text="Tipo de produto, identificado por uma abreviatura de 4 letras")
    nome = CharField(max_length=40, blank=False, unique=True, verbose_name="Nome do Produto", help_text="Nome do produto por extenso")
    descricao = TextField(verbose_name="Descrição do Produto", help_text="Descrição do Produto")

class DocOS(Model):

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'

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

class DocPE(Model):

    class Meta:
        verbose_name = 'Projeto Especial'
        verbose_name_plural = 'Projetos Especiais'
        
class DocEV(Model):

    class Meta:
        verbose_name = 'Estudo de Viabilidade'
        verbose_name_plural = 'Estudos de Viabilidade'
