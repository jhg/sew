# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grupo'
        db.create_table('usuarios_grupo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('usuarios', ['Grupo'])

        # Adding unique constraint on 'TipoAutenticacion', fields ['nombre']
        db.create_unique('usuarios_tipoautenticacion', ['nombre'])

        # Adding M2M table for field grupo on 'Usuario'
        db.create_table('usuarios_usuario_grupo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm['usuarios.usuario'], null=False)),
            ('grupo', models.ForeignKey(orm['usuarios.grupo'], null=False))
        ))
        db.create_unique('usuarios_usuario_grupo', ['usuario_id', 'grupo_id'])

        # Adding unique constraint on 'Usuario', fields ['nombre']
        db.create_unique('usuarios_usuario', ['nombre'])


    def backwards(self, orm):
        # Removing unique constraint on 'Usuario', fields ['nombre']
        db.delete_unique('usuarios_usuario', ['nombre'])

        # Removing unique constraint on 'TipoAutenticacion', fields ['nombre']
        db.delete_unique('usuarios_tipoautenticacion', ['nombre'])

        # Deleting model 'Grupo'
        db.delete_table('usuarios_grupo')

        # Removing M2M table for field grupo on 'Usuario'
        db.delete_table('usuarios_usuario_grupo')


    models = {
        'usuarios.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'usuarios.tipoautenticacion': {
            'Meta': {'object_name': 'TipoAutenticacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'grupo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['usuarios.Grupo']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'tipo_de_autenticacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['usuarios.TipoAutenticacion']"}),
            'valor_de_autenticacion': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['usuarios']