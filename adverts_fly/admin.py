#-*- coding: UTF-8 -*-
from adverts_fly.models import AdvertsFlySiteConfiguration
from adverts_fly.models import AdvertsFlyExcludeDomain
from django.contrib import admin

admin.site.register(AdvertsFlySiteConfiguration)
admin.site.register(AdvertsFlyExcludeDomain)
