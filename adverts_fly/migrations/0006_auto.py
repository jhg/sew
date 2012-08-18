# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field exclude_domains on 'AdvertsFlySiteConfiguration'
        db.delete_table('adverts_fly_advertsflysiteconfiguration_exclude_domains')

        # Adding M2M table for field excludes_domains on 'AdvertsFlySiteConfiguration'
        db.create_table('adverts_fly_advertsflysiteconfiguration_excludes_domains', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advertsflysiteconfiguration', models.ForeignKey(orm['adverts_fly.advertsflysiteconfiguration'], null=False)),
            ('advertsflyexcludedomain', models.ForeignKey(orm['adverts_fly.advertsflyexcludedomain'], null=False))
        ))
        db.create_unique('adverts_fly_advertsflysiteconfiguration_excludes_domains', ['advertsflysiteconfiguration_id', 'advertsflyexcludedomain_id'])


    def backwards(self, orm):
        # Adding M2M table for field exclude_domains on 'AdvertsFlySiteConfiguration'
        db.create_table('adverts_fly_advertsflysiteconfiguration_exclude_domains', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advertsflysiteconfiguration', models.ForeignKey(orm['adverts_fly.advertsflysiteconfiguration'], null=False)),
            ('advertsflyexcludedomain', models.ForeignKey(orm['adverts_fly.advertsflyexcludedomain'], null=False))
        ))
        db.create_unique('adverts_fly_advertsflysiteconfiguration_exclude_domains', ['advertsflysiteconfiguration_id', 'advertsflyexcludedomain_id'])

        # Removing M2M table for field excludes_domains on 'AdvertsFlySiteConfiguration'
        db.delete_table('adverts_fly_advertsflysiteconfiguration_excludes_domains')


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
            'exclude_self_domain': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'excludes_domains': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['adverts_fly.AdvertsFlyExcludeDomain']", 'symmetrical': 'False', 'blank': 'True'}),
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