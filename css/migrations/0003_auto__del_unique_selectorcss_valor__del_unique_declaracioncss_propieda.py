# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'DeclaracionCss', fields ['valor']
        db.delete_unique('css_declaracioncss', ['valor'])

        # Removing unique constraint on 'DeclaracionCss', fields ['propiedad']
        db.delete_unique('css_declaracioncss', ['propiedad'])

        # Removing unique constraint on 'SelectorCss', fields ['valor']
        db.delete_unique('css_selectorcss', ['valor'])


    def backwards(self, orm):
        # Adding unique constraint on 'SelectorCss', fields ['valor']
        db.create_unique('css_selectorcss', ['valor'])

        # Adding unique constraint on 'DeclaracionCss', fields ['propiedad']
        db.create_unique('css_declaracioncss', ['propiedad'])

        # Adding unique constraint on 'DeclaracionCss', fields ['valor']
        db.create_unique('css_declaracioncss', ['valor'])


    models = {
        'css.declaracioncss': {
            'Meta': {'object_name': 'DeclaracionCss'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propiedad': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'selectorCss': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['css.SelectorCss']", 'symmetrical': 'False'}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'css.hojacss': {
            'Meta': {'object_name': 'HojaCss'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'css.selectorcss': {
            'Meta': {'object_name': 'SelectorCss'},
            'hojaCss': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['css.HojaCss']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['css']