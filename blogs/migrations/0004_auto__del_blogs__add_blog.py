# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Blogs'
        db.delete_table('blogs_blogs')

        # Adding model 'Blog'
        db.create_table('blogs_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('blogs', ['Blog'])


    def backwards(self, orm):
        # Adding model 'Blogs'
        db.create_table('blogs_blogs', (
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('blogs', ['Blogs'])

        # Deleting model 'Blog'
        db.delete_table('blogs_blog')


    models = {
        'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['blogs']