# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Ingrediente_Receta'
        db.delete_table('recetas_ingrediente_receta')

        # Deleting model 'Paso_Elaboacion_Receta'
        db.delete_table('recetas_paso_elaboacion_receta')

        # Adding model 'PasoElaboacionReceta'
        db.create_table('recetas_pasoelaboacionreceta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('receta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recetas.Receta'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', max_length=1024)),
        ))
        db.send_create_signal('recetas', ['PasoElaboacionReceta'])

        # Adding model 'IngredienteReceta'
        db.create_table('recetas_ingredientereceta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('receta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recetas.Receta'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=64)),
            ('detalles', self.gf('django.db.models.fields.TextField')(default='', max_length=256, blank=True)),
        ))
        db.send_create_signal('recetas', ['IngredienteReceta'])


    def backwards(self, orm):
        # Adding model 'Ingrediente_Receta'
        db.create_table('recetas_ingrediente_receta', (
            ('detalles', self.gf('django.db.models.fields.TextField')(default='', max_length=256, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=64)),
            ('receta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recetas.Receta'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('recetas', ['Ingrediente_Receta'])

        # Adding model 'Paso_Elaboacion_Receta'
        db.create_table('recetas_paso_elaboacion_receta', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', max_length=1024)),
            ('receta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recetas.Receta'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('recetas', ['Paso_Elaboacion_Receta'])

        # Deleting model 'PasoElaboacionReceta'
        db.delete_table('recetas_pasoelaboacionreceta')

        # Deleting model 'IngredienteReceta'
        db.delete_table('recetas_ingredientereceta')


    models = {
        'recetas.ingredientereceta': {
            'Meta': {'object_name': 'IngredienteReceta'},
            'detalles': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'receta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recetas.Receta']"})
        },
        'recetas.pasoelaboacionreceta': {
            'Meta': {'object_name': 'PasoElaboacionReceta'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recetas.Receta']"})
        },
        'recetas.receta': {
            'Meta': {'object_name': 'Receta'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'})
        }
    }

    complete_apps = ['recetas']