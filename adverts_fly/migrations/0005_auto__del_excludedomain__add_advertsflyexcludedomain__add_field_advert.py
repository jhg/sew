# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ExcludeDomain'
        db.delete_table('adverts_fly_excludedomain')

        # Adding model 'AdvertsFlyExcludeDomain'
        db.create_table('adverts_fly_advertsflyexcludedomain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('adverts_fly', ['AdvertsFlyExcludeDomain'])

        # Adding field 'AdvertsFlySiteConfiguration.exclude_self_domain'
        db.add_column('adverts_fly_advertsflysiteconfiguration', 'exclude_self_domain',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'ExcludeDomain'
        db.create_table('adverts_fly_excludedomain', (
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=256, blank=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('adverts_fly', ['ExcludeDomain'])

        # Deleting model 'AdvertsFlyExcludeDomain'
        db.delete_table('adverts_fly_advertsflyexcludedomain')

        # Deleting field 'AdvertsFlySiteConfiguration.exclude_self_domain'
        db.delete_column('adverts_fly_advertsflysiteconfiguration', 'exclude_self_domain')


    models = {
        'adverts_fly.advertsflyexcludedomain': {
            'Meta': {'object_name': 'AdvertsFlyExcludeDomain'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'adverts_fly.advertsflysiteconfiguration': {
            'Meta': {'object_name': 'AdvertsFlySiteConfiguration'},
            'adverts_links_domain': ('django.db.models.fields.CharField', [], {'default': "'adf.ly'", 'max_length': '32'}),
            'adverts_type': ('django.db.models.fields.CharField', [], {'default': "'int'", 'max_length': '8'}),
            'exclude_domains': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['adverts_fly.AdvertsFlyExcludeDomain']", 'symmetrical': 'False', 'blank': 'True'}),
            'exclude_self_domain': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['adverts_fly']