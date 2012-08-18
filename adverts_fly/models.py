from django.db import models
from django.contrib.sites.models import Site

ADVERTS_FLY_DOMAINS = (
    ('adf.ly', 'adf.ly'),
    ('q.gs', 'q.gs'),
)

ADVERTS_FLY_TYPES = (
    ('int', 'int'),
    ('banner', 'banner'),
)

class AdvertsFlyExcludeDomain(models.Model):
    domain = models.CharField(max_length=32, blank=False)
    comment = models.TextField(max_length=256, blank=True)

    def __unicode__(self):
        return self.domain

class AdvertsFlySiteConfiguration(models.Model):
    site = models.OneToOneField(Site, blank=False)
    uid = models.CharField(max_length=8, blank=False)
    key = models.CharField(max_length=32, blank=False)
    adverts_links_domain = models.CharField(max_length=32,
        choices=ADVERTS_FLY_DOMAINS, default="adf.ly", blank=False)
    adverts_type = models.CharField(max_length=8,
        choices=ADVERTS_FLY_TYPES, default="int", blank=False)
    exclude_self_domain = models.BooleanField(default=True)
    excludes_domains = models.ManyToManyField(AdvertsFlyExcludeDomain,
        blank=True)

    def __unicode__(self):
        return self.site.domain
    
