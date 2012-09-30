from django.contrib.sites.models import Site
from django.db import models


# Domains for short link with advert, view adf.ly API
ADVERTS_FLY_DOMAINS = (
    ('adf.ly', 'adf.ly'),
    ('q.gs', 'q.gs'),
)

# Type of advert in short link, view adf.ly API
ADVERTS_FLY_TYPES = (
    ('int', _('Interstitial')),
    ('banner', _('Banner')),
)

# Exclude domain of short link with advert
class AdvertsFlyExcludeDomain(models.Model):
    domain = models.CharField(max_length=32, blank=False)
    comment = models.TextField(max_length=256, blank=True)

    def __unicode__(self):
        return self.domain + ' - ' + self.comment[:32]

# Configuration for site
class AdvertsFlySiteConfiguration(models.Model):
    sites = models.ManyToManyField(Site, blank=False)
    uid = models.CharField(max_length=8, blank=False) # view adf.ly API
    key = models.CharField(max_length=32, blank=False)# view adf.ly API
    adverts_links_domain = models.CharField(max_length=32,
        choices=ADVERTS_FLY_DOMAINS, default="adf.ly", blank=False)
    adverts_type = models.CharField(max_length=8,
        choices=ADVERTS_FLY_TYPES, default="int", blank=False)
    exclude_self_domain = models.BooleanField(default=True)
    exclude_domains = models.ManyToManyField(AdvertsFlyExcludeDomain,
        blank=True)

    def __unicode__(self):
        return self.get_adverts_type_display().lower() + ' ' + \
            self.get_adverts_links_domain_display() + ' ' + \
            self.uid + ' ' + self.key
