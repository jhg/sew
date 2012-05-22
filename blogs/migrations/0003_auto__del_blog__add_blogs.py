# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table('blogs_blog')

        # Adding model 'Blogs'
        db.create_table('blogs_blogs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('blogs', ['Blogs'])


    def backwards(self, orm):
        # Adding model 'Blog'
        db.create_table('blogs_blog', (
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('blogs', ['Blog'])

        # Deleting model 'Blogs'
        db.delete_table('blogs_blogs')


    models = {
        'blogs.blogs': {
            'Meta': {'object_name': 'Blogs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['blogs']