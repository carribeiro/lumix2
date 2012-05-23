# coding: utf-8
from collections import OrderedDict
import json
import csv

__author__ = 'cribeiro'

def make_os(os):
    os
    return os
    ref_os =
    #ref_doc = ForeignKey(Documento, related_name) # TODO: verificar o jeito certo de fazer isso, com herança, ou referenciando o documento
    criado_por =
    data_criacao =
    tipo_os =
    documento_origem =
    prazo =
    previsao_entrega =
    produto =
    velocidade =
    num_ips =
    cliente =
    usuario_final =
    titulo =
    descricao =
    endereco_atendido =
    etapa =
    situacao =


OS_FIELD_NAMES = ['ref_os', 'criado_por', 'tipo_os', 'data_criacao', 'documento_origem', 'prazo',
                  'previsao_entrega', 'produto', 'velocidade', 'num_ips', 'cliente', 'usuario_final',
                  'descricao', 'endereco_atendido', 'etapa']

OS_EXTRA_FIELD_NAMES = ['titulo']

# converte as OSs
i = 0
with open('os2011.csv', 'rb') as src:
    rdr = csv.DictReader(src, fieldnames=OS_FIELD_NAMES)
    fixture = []
    for row in rdr:
        if row['ref_os'] != '':
            i = i+1
            entry = OrderedDict()
            entry['model'] = 'lumixcore.os'
            entry['pk'] = i
            entry['fields'] = row
            fixture.append(entry)
            #print i, row[rdr.fieldnames[0]]
with open('os2012.csv', 'rb') as src:
    rdr = csv.DictReader(src, fieldnames=OS_FIELD_NAMES)
    fixture = []
    for row in rdr:
        if row['ref_os'] != '':
            i = i+1
            entry = OrderedDict()
            entry['model'] = 'lumixcore.os'
            entry['pk'] = i
            entry['fields'] = row
            fixture.append(entry)
            #print i, row[rdr.fieldnames[0]]
with open('os.json', 'wb') as outfile:
    json.dump(fixture, outfile, indent=4)


