# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SitesConfiguration'
        db.delete_table('adverts_fly_sitesconfiguration')

        # Removing M2M table for field exclude_domains on 'SitesConfiguration'
        db.delete_table('adverts_fly_sitesconfiguration_exclude_domains')

        # Adding model 'AdvertsFlySitesConfiguration'
        db.create_table('adverts_fly_advertsflysitesconfiguration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
            ('adverts_links_domain', self.gf('django.db.models.fields.CharField')(default='adf.ly', max_length=32)),
            ('exclude_internal_links', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('adverts_fly', ['AdvertsFlySitesConfiguration'])

        # Adding M2M table for field exclude_domains on 'AdvertsFlySitesConfiguration'
        db.create_table('adverts_fly_advertsflysitesconfiguration_exclude_domains', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advertsflysitesconfiguration', models.ForeignKey(orm['adverts_fly.advertsflysitesconfiguration'], null=False)),
            ('excludedomain', models.ForeignKey(orm['adverts_fly.excludedomain'], null=False))
        ))
        db.create_unique('adverts_fly_advertsflysitesconfiguration_exclude_domains', ['advertsflysitesconfiguration_id', 'excludedomain_id'])


    def backwards(self, orm):
        # Adding model 'SitesConfiguration'
        db.create_table('adverts_fly_sitesconfiguration', (
            ('adverts_links_domain', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
            ('exclude_internal_links', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('adverts_fly', ['SitesConfiguration'])

        # Adding M2M table for field exclude_domains on 'SitesConfiguration'
        db.create_table('adverts_fly_sitesconfiguration_exclude_domains', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sitesconfiguration', models.ForeignKey(orm['adverts_fly.sitesconfiguration'], null=False)),
            ('excludedomain', models.ForeignKey(orm['adverts_fly.excludedomain'], null=False))
        ))
        db.create_unique('adverts_fly_sitesconfiguration_exclude_domains', ['sitesconfiguration_id', 'excludedomain_id'])

        # Deleting model 'AdvertsFlySitesConfiguration'
        db.delete_table('adverts_fly_advertsflysitesconfiguration')

        # Removing M2M table for field exclude_domains on 'AdvertsFlySitesConfiguration'
        db.delete_table('adverts_fly_advertsflysitesconfiguration_exclude_domains')


    models = {
        'adverts_fly.advertsflysitesconfiguration': {
            'Meta': {'object_name': 'AdvertsFlySitesConfiguration'},
            'adverts_links_domain': ('django.db.models.fields.CharField', [], {'default': "'adf.ly'", 'max_length': '32'}),
            'exclude_domains': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['adverts_fly.ExcludeDomain']", 'symmetrical': 'False', 'blank': 'True'}),
            'exclude_internal_links': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True'})
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