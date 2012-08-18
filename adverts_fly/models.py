from django.db import models
from django.contrib.sites.models import Site

ADVERTS_FLY_DOMAINS = (
    ('adf.ly', 'adf.ly'),
    ('q.gs', 'q.gs'),
)

class ExcludeDomain(models.Model):
    domain = models.CharField(max_length=32, blank=False)
    comment = models.TextField(max_length=256, blank=True)

    def __unicode__(self):
        return self.domain

class AdvertsFlySitesConfiguration(models.Model):
    site = models.OneToOneField(Site, blank=False)
    adverts_links_domain = models.CharField(max_length=32,
        choices=ADVERTS_FLY_DOMAINS, default="adf.ly", blank=False)
    exclude_internal_links = models.BooleanField(default=True)
    exclude_domains = models.ManyToManyField(ExcludeDomain, blank=True)
