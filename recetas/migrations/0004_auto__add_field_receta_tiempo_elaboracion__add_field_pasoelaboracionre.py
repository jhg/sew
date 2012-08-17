# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Receta.tiempo_elaboracion'
        db.add_column('recetas_receta', 'tiempo_elaboracion',
                      self.gf('django.db.models.fields.TimeField')(default='00:15:00'),
                      keep_default=False)

        # Adding field 'PasoElaboracionReceta.numero_paso'
        db.add_column('recetas_pasoelaboracionreceta', 'numero_paso',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'IngredienteReceta.cantidad'
        db.add_column('recetas_ingredientereceta', 'cantidad',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=3),
                      keep_default=False)

        # Adding field 'IngredienteReceta.unidad'
        db.add_column('recetas_ingredientereceta', 'unidad',
                      self.gf('django.db.models.fields.CharField')(default='u', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Receta.tiempo_elaboracion'
        db.delete_column('recetas_receta', 'tiempo_elaboracion')

        # Deleting field 'PasoElaboracionReceta.numero_paso'
        db.delete_column('recetas_pasoelaboracionreceta', 'numero_paso')

        # Deleting field 'IngredienteReceta.cantidad'
        db.delete_column('recetas_ingredientereceta', 'cantidad')

        # Deleting field 'IngredienteReceta.unidad'
        db.delete_column('recetas_ingredientereceta', 'unidad')


    models = {
        'recetas.ingredientereceta': {
            'Meta': {'object_name': 'IngredienteReceta'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '3'}),
            'detalles': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'receta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recetas.Receta']"}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'recetas.pasoelaboracionreceta': {
            'Meta': {'object_name': 'PasoElaboracionReceta'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_paso': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'receta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recetas.Receta']"})
        },
        'recetas.receta': {
            'Meta': {'object_name': 'Receta'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'tiempo_elaboracion': ('django.db.models.fields.TimeField', [], {'default': "'00:15:00'"})
        }
    }

    complete_apps = ['recetas']