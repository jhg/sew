# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoAutenticacion'
        db.create_table('usuarios_tipoautenticacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('usuarios', ['TipoAutenticacion'])

        # Adding model 'Usuario'
        db.create_table('usuarios_usuario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('tipo_de_autenticacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.TipoAutenticacion'])),
            ('valor_de_autenticacion', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('usuarios', ['Usuario'])


    def backwards(self, orm):
        # Deleting model 'TipoAutenticacion'
        db.delete_table('usuarios_tipoautenticacion')

        # Deleting model 'Usuario'
        db.delete_table('usuarios_usuario')


    models = {
        'usuarios.tipoautenticacion': {
            'Meta': {'object_name': 'TipoAutenticacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'tipo_de_autenticacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['usuarios.TipoAutenticacion']"}),
            'valor_de_autenticacion': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['usuarios']