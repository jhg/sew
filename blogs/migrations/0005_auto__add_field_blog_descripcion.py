# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.descripcion'
        db.add_column('blogs_blog', 'descripcion',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blog.descripcion'
        db.delete_column('blogs_blog', 'descripcion')


    models = {
        'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'})
        }
    }

    complete_apps = ['blogs']