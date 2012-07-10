from blogs.models import Blog
from django.shortcuts import render_to_response
from django.conf import settings
from django.contrib.sites.models import Site


def index(request):
    return render_to_response('construccion.htm')
