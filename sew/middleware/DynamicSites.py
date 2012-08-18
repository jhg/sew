#-*- coding: UTF-8 -*-
""" For use middleware: <app>.middleware.DynamicSites.SetDynamicSites
from <app>.middleware.DynamicSites import DynamicSiteId, SITE_THREAD_INFO
SITE_ID = DynamicSiteId()
MEDIA_URL_DIR = '/cargas/'
STATIC_URL_DIR = '/estaticos/' """
from threading import local
from django.conf import settings
from django.contrib.sites.models import Site
import re


class SetDynamicSites(object):
    """ Change SITE_ID dinamics. """
    def process_request(self, request):
        try:
            current_site = Site.objects.get(domain=request.get_host())
            settings.SITE_ID._set(current_site.id)
            settings.MEDIA_URL = '//' + request.get_host() + \
                settings.MEDIA_URL_DIR
            settings.STATIC_URL = '//' + request.get_host() + \
                settings.STATIC_URL_DIR
            settings.HOST = request.get_host()
        except:
            settings.SITE_ID._set(1)
        return None


SITE_THREAD_INFO = local()


class DynamicSiteId(object):
    def __init__(self):
        SITE_THREAD_INFO.SITE_ID = 1

    def __unicode__(self):
        try:
            return unicode(SITE_THREAD_INFO.SITE_ID)
        except AttributeError:
            SITE_THREAD_INFO.SITE_ID = 1
            return unicode(SITE_THREAD_INFO.SITE_ID)

    def __str__(self):
        try:
            return str(SITE_THREAD_INFO.SITE_ID)
        except AttributeError:
            SITE_THREAD_INFO.SITE_ID = 1
            return str(SITE_THREAD_INFO.SITE_ID)

    def __hash__(self):
        try:
            return SITE_THREAD_INFO.SITE_ID
        except AttributeError:
            SITE_THREAD_INFO.SITE_ID = 1
            return SITE_THREAD_INFO.SITE_ID

    def __int__(self):
        try:
            return SITE_THREAD_INFO.SITE_ID
        except AttributeError:
            SITE_THREAD_INFO.SITE_ID = 1
            return SITE_THREAD_INFO.SITE_ID

    def _set(self, value):
        SITE_THREAD_INFO.SITE_ID = int(value)
