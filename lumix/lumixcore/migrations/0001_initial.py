# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoDocumento'
        db.create_table('lumixcore_tipodocumento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_documento', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('mascara', self.gf('django.db.models.fields.CharField')(max_length=14)),
        ))
        db.send_create_signal('lumixcore', ['TipoDocumento'])

        # Adding model 'Documento'
        db.create_table('lumixcore_documento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ref_doc', self.gf('django.db.models.fields.CharField')(unique=True, max_length=14)),
            ('tipo_documento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lumixcore.TipoDocumento'])),
        ))
        db.send_create_signal('lumixcore', ['Documento'])

        # Adding model 'Conta'
        db.create_table('lumixcore_conta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_conta', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
        ))
        db.send_create_signal('lumixcore', ['Conta'])

        # Adding model 'Produto'
        db.create_table('lumixcore_produto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_produto', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('lumixcore', ['Produto'])

        # Adding model 'OS'
        db.create_table('lumixcore_os', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ref_os', self.gf('django.db.models.fields.CharField')(unique=True, max_length=14)),
            ('criado_por', self.gf('django.db.models.fields.related.ForeignKey')(related_name='os_criadas', to=orm['auth.User'])),
            ('data_criacao', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('tipo_os', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('documento_origem', self.gf('django.db.models.fields.related.ForeignKey')(related_name='documentos_originados', to=orm['lumixcore.Documento'])),
            ('prazo', self.gf('django.db.models.fields.IntegerField')()),
            ('previsao_entrega', self.gf('django.db.models.fields.DateField')()),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='produtos', to=orm['lumixcore.Produto'])),
            ('velocidade', self.gf('django.db.models.fields.IntegerField')()),
            ('num_ips', self.gf('django.db.models.fields.IntegerField')()),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clientes', to=orm['lumixcore.Conta'])),
            ('usuario_final', self.gf('django.db.models.fields.related.ForeignKey')(related_name='usuarios_finais', to=orm['lumixcore.Conta'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('endereco_atendido', self.gf('django.db.models.fields.TextField')()),
            ('etapa', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('lumixcore', ['OS'])


    def backwards(self, orm):
        # Deleting model 'TipoDocumento'
        db.delete_table('lumixcore_tipodocumento')

        # Deleting model 'Documento'
        db.delete_table('lumixcore_documento')

        # Deleting model 'Conta'
        db.delete_table('lumixcore_conta')

        # Deleting model 'Produto'
        db.delete_table('lumixcore_produto')

        # Deleting model 'OS'
        db.delete_table('lumixcore_os')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lumixcore.conta': {
            'Meta': {'object_name': 'Conta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_conta': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        'lumixcore.documento': {
            'Meta': {'object_name': 'Documento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref_doc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '14'}),
            'tipo_documento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lumixcore.TipoDocumento']"})
        },
        'lumixcore.os': {
            'Meta': {'object_name': 'OS'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clientes'", 'to': "orm['lumixcore.Conta']"}),
            'criado_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'os_criadas'", 'to': "orm['auth.User']"}),
            'data_criacao': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'documento_origem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documentos_originados'", 'to': "orm['lumixcore.Documento']"}),
            'endereco_atendido': ('django.db.models.fields.TextField', [], {}),
            'etapa': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_ips': ('django.db.models.fields.IntegerField', [], {}),
            'prazo': ('django.db.models.fields.IntegerField', [], {}),
            'previsao_entrega': ('django.db.models.fields.DateField', [], {}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'produtos'", 'to': "orm['lumixcore.Produto']"}),
            'ref_os': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '14'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'tipo_os': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'usuario_final': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usuarios_finais'", 'to': "orm['lumixcore.Conta']"}),
            'velocidade': ('django.db.models.fields.IntegerField', [], {})
        },
        'lumixcore.produto': {
            'Meta': {'object_name': 'Produto'},
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'tipo_produto': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'})
        },
        'lumixcore.tipodocumento': {
            'Meta': {'object_name': 'TipoDocumento'},
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mascara': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'tipo_documento': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'})
        }
    }

    complete_apps = ['lumixcore']