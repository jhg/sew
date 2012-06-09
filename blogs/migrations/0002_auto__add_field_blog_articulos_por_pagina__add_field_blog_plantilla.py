# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.articulos_por_pagina'
        db.add_column('blogs_blog', 'articulos_por_pagina',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Blog.plantilla'
        db.add_column('blogs_blog', 'plantilla',
                      self.gf('django.db.models.fields.TextField')(default='<html>\n<head></head>\n<body></body></html>', max_length=8192),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blog.articulos_por_pagina'
        db.delete_column('blogs_blog', 'articulos_por_pagina')

        # Deleting field 'Blog.plantilla'
        db.delete_column('blogs_blog', 'plantilla')


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
        'blogs.articulo': {
            'Meta': {'object_name': 'Articulo'},
            'autores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'blog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blogs.Blog']", 'symmetrical': 'False'}),
            'bloqueado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'colectivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publicacion': ('django.db.models.fields.DateTimeField', [], {}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'})
        },
        'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'articulos_por_pagina': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'autores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'bloqueado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'colectivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'plantilla': ('django.db.models.fields.TextField', [], {'default': "'<html>\\n<head></head>\\n<body></body></html>'", 'max_length': '8192'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'url': ('django.db.models.fields.SlugField', [], {'default': "''", 'unique': 'True', 'max_length': '64'})
        },
        'blogs.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'articulo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Articulo']"}),
            'autor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'texto': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '256'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blogs']