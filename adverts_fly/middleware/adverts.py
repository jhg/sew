#-*- coding: UTF-8 -*-
""" Middleware for use links adverts of adf.ly in your site.
For use middleware:
    adverts_fly.middleware.adverts.ChangeLinks

In settings configure:
ADVERTS_FLY_UID = <your_uid>
ADVERTS_FLY_KEY = <your_key>
ADVERTS_FLY_TYPE = 'int' # Or 'banner'
ADVERTS_FLY_DOMAIN = 'adf.ly' # Or 'q.gs' """
from django.conf import settings
import re
import urllib, urllib2


CONFIG = {
    'SECURE_LINKS': False,
    'REQUEST_DOMAIN': '',
    }

def _Link2Advert(match):
    """ Replace links for adverts links in all links finded """
    link = match.group('link')
    # Check if is internal link
    if link[0] == '/' and link[1] != '/':
        return match.group()
    # Check protocol for make a full link correct
    if CONFIG['SECURE_LINKS']:
        protocol = 'https://'
    else:
        protocol = 'http://'
    # Make full link correct if is necesary
    all_link = re.sub(r'^//', protocol, link)
    # Check if is internal link
    if not re.match(r'^http[s]?://', all_link, re.IGNORECASE|re.UNICODE):
        return match.group()
    domain = all_link.split('/')[2]
    if domain == CONFIG['REQUEST_DOMAIN']:
        return match.group()
    # Encode params
    params = urllib.urlencode({
        'uid': settings.ADVERTS_FLY_UID,
        'key': settings.ADVERTS_FLY_KEY,
        'advert_type': settings.ADVERTS_FLY_TYPE,
        'domain': settings.ADVERTS_FLY_DOMAIN,
        'url': all_link,
        })
    # Get short url with advert
    api_adverts = urllib2.urlopen('http://api.adf.ly/api.php?' + params)
    ad_link = api_adverts.read().strip()
    api_adverts.close()
    # Check if all right
    if ad_link == 'error':
        return match.group()
    # Replace original links for adverts links
    return re.sub(link, ad_link, match.group())

class ChangeLinks(object):
    """ Change links for advertise links of adfly. """
    def process_response(self, request, response):
        if response.get('content-type').split(';')[0] == 'text/html':
            CONFIG['SECURE_LINKS'] = request.is_secure()
            CONFIG['REQUEST_DOMAIN'] = request.get_host()
            patron_1 = re.compile(r"<a(?P<prev>[ a-zA-Z0-9_='\"]*)"
                + r"href='(?P<link>\S+)'(?P<next>[ a-zA-Z0-9_='\"]*)>",
                re.IGNORECASE|re.MULTILINE|re.UNICODE)
            patron_2 = re.compile(r'<a(?P<prev>[ a-zA-Z0-9_="\']*)'
                + r'href="(?P<link>\S+)"(?P<next>[ a-zA-Z0-9_="\']*)>',
                re.IGNORECASE|re.MULTILINE|re.UNICODE)
            try:
                response.content = patron_1.sub(_Link2Advert, response.content)
            except:
                pass
            try:
                response.content = patron_2.sub(_Link2Advert, response.content)
            except:
                pass
        return response
