# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AdvertsFlySiteConfiguration.exclude_internal_links'
        db.delete_column('adverts_fly_advertsflysiteconfiguration', 'exclude_internal_links')

        # Adding field 'AdvertsFlySiteConfiguration.uid'
        db.add_column('adverts_fly_advertsflysiteconfiguration', 'uid',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=8),
                      keep_default=False)

        # Adding field 'AdvertsFlySiteConfiguration.key'
        db.add_column('adverts_fly_advertsflysiteconfiguration', 'key',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)

        # Adding field 'AdvertsFlySiteConfiguration.adverts_type'
        db.add_column('adverts_fly_advertsflysiteconfiguration', 'adverts_type',
                      self.gf('django.db.models.fields.CharField')(default='int', max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'AdvertsFlySiteConfiguration.exclude_internal_links'
        db.add_column('adverts_fly_advertsflysiteconfiguration', 'exclude_internal_links',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'AdvertsFlySiteConfiguration.uid'
        db.delete_column('adverts_fly_advertsflysiteconfiguration', 'uid')

        # Deleting field 'AdvertsFlySiteConfiguration.key'
        db.delete_column('adverts_fly_advertsflysiteconfiguration', 'key')

        # Deleting field 'AdvertsFlySiteConfiguration.adverts_type'
        db.delete_column('adverts_fly_advertsflysiteconfiguration', 'adverts_type')


    models = {
        'adverts_fly.advertsflysiteconfiguration': {
            'Meta': {'object_name': 'AdvertsFlySiteConfiguration'},
            'adverts_links_domain': ('django.db.models.fields.CharField', [], {'default': "'adf.ly'", 'max_length': '32'}),
            'adverts_type': ('django.db.models.fields.CharField', [], {'default': "'int'", 'max_length': '8'}),
            'exclude_domains': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['adverts_fly.ExcludeDomain']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'adverts_fly.excludedomain': {
            'Meta': {'object_name': 'ExcludeDomain'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['adverts_fly']