# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TipoAutenticacion.modulo'
        db.add_column('usuarios_tipoautenticacion', 'modulo',
                      self.gf('django.db.models.fields.CharField')(default=None, unique=True, max_length=64),
                      keep_default=False)

        # Deleting field 'Usuario.es_anonimo'
        db.delete_column('usuarios_usuario', 'es_anonimo')


    def backwards(self, orm):
        # Deleting field 'TipoAutenticacion.modulo'
        db.delete_column('usuarios_tipoautenticacion', 'modulo')

        # Adding field 'Usuario.es_anonimo'
        db.add_column('usuarios_usuario', 'es_anonimo',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        'usuarios.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'usuarios.tipoautenticacion': {
            'Meta': {'object_name': 'TipoAutenticacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'grupo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['usuarios.Grupo']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_usuario': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'tipo_de_autenticacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['usuarios.TipoAutenticacion']"}),
            'valor_de_autenticacion': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['usuarios']