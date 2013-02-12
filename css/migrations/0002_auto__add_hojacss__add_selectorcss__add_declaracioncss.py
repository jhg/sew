# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HojaCss'
        db.create_table('css_hojacss', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('css', ['HojaCss'])

        # Adding model 'SelectorCss'
        db.create_table('css_selectorcss', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('valor', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('css', ['SelectorCss'])

        # Adding M2M table for field hojaCss on 'SelectorCss'
        db.create_table('css_selectorcss_hojaCss', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('selectorcss', models.ForeignKey(orm['css.selectorcss'], null=False)),
            ('hojacss', models.ForeignKey(orm['css.hojacss'], null=False))
        ))
        db.create_unique('css_selectorcss_hojaCss', ['selectorcss_id', 'hojacss_id'])

        # Adding model 'DeclaracionCss'
        db.create_table('css_declaracioncss', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('propiedad', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('valor', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('css', ['DeclaracionCss'])

        # Adding M2M table for field selectorCss on 'DeclaracionCss'
        db.create_table('css_declaracioncss_selectorCss', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('declaracioncss', models.ForeignKey(orm['css.declaracioncss'], null=False)),
            ('selectorcss', models.ForeignKey(orm['css.selectorcss'], null=False))
        ))
        db.create_unique('css_declaracioncss_selectorCss', ['declaracioncss_id', 'selectorcss_id'])


    def backwards(self, orm):
        # Deleting model 'HojaCss'
        db.delete_table('css_hojacss')

        # Deleting model 'SelectorCss'
        db.delete_table('css_selectorcss')

        # Removing M2M table for field hojaCss on 'SelectorCss'
        db.delete_table('css_selectorcss_hojaCss')

        # Deleting model 'DeclaracionCss'
        db.delete_table('css_declaracioncss')

        # Removing M2M table for field selectorCss on 'DeclaracionCss'
        db.delete_table('css_declaracioncss_selectorCss')


    models = {
        'css.declaracioncss': {
            'Meta': {'object_name': 'DeclaracionCss'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propiedad': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'selectorCss': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['css.SelectorCss']", 'symmetrical': 'False'}),
            'valor': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
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
            'valor': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        }
    }

    complete_apps = ['css']