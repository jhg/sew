#-*- coding: UTF-8 -*-
from adverts_fly.models import AdvertsFlySiteConfiguration, ExcludeDomain
from django.contrib import admin

admin.site.register(AdvertsFlySiteConfiguration)
admin.site.register(ExcludeDomain)
