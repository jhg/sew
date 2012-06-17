# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table('blogs_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(default='', max_length=64)),
            ('url', self.gf('django.db.models.fields.SlugField')(default='', unique=True, max_length=64)),
            ('publicado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bloqueado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', max_length=256, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('blogs', ['Blog'])

        # Adding M2M table for field autores on 'Blog'
        db.create_table('blogs_blog_autores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm['blogs.blog'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('blogs_blog_autores', ['blog_id', 'user_id'])

        # Adding M2M table for field colectivos on 'Blog'
        db.create_table('blogs_blog_colectivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm['blogs.blog'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('blogs_blog_colectivos', ['blog_id', 'group_id'])

        # Adding model 'Articulo'
        db.create_table('blogs_articulo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('contenido', self.gf('django.db.models.fields.TextField')(default='')),
            ('publicado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bloqueado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('publicacion', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal('blogs', ['Articulo'])

        # Adding M2M table for field blog on 'Articulo'
        db.create_table('blogs_articulo_blog', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm['blogs.articulo'], null=False)),
            ('blog', models.ForeignKey(orm['blogs.blog'], null=False))
        ))
        db.create_unique('blogs_articulo_blog', ['articulo_id', 'blog_id'])

        # Adding M2M table for field autores on 'Articulo'
        db.create_table('blogs_articulo_autores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm['blogs.articulo'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('blogs_articulo_autores', ['articulo_id', 'user_id'])

        # Adding M2M table for field colectivos on 'Articulo'
        db.create_table('blogs_articulo_colectivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm['blogs.articulo'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('blogs_articulo_colectivos', ['articulo_id', 'group_id'])

        # Adding model 'Comentario'
        db.create_table('blogs_comentario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('articulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogs.Articulo'])),
            ('autor', self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(default='', max_length=256)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('moderado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('blogs', ['Comentario'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table('blogs_blog')

        # Removing M2M table for field autores on 'Blog'
        db.delete_table('blogs_blog_autores')

        # Removing M2M table for field colectivos on 'Blog'
        db.delete_table('blogs_blog_colectivos')

        # Deleting model 'Articulo'
        db.delete_table('blogs_articulo')

        # Removing M2M table for field blog on 'Articulo'
        db.delete_table('blogs_articulo_blog')

        # Removing M2M table for field autores on 'Articulo'
        db.delete_table('blogs_articulo_autores')

        # Removing M2M table for field colectivos on 'Articulo'
        db.delete_table('blogs_articulo_colectivos')

        # Deleting model 'Comentario'
        db.delete_table('blogs_comentario')


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
            'publicacion': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'})
        },
        'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'autores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'bloqueado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'colectivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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
