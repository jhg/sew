from blogs.models import Blog
from django.shortcuts import render_to_response
from django.conf import settings


def index(request):
    idsite = settings.SITE_ID
    return render_to_response('construccion.htm', {"idsite": idsite})
