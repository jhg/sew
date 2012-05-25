from blogs.models import Blog
from django.shortcuts import render_to_response
from settings_local import HOST

def index(request):
    blogs = Blog.objects.all()
    num_blogs = len(blogs)
    return render_to_response('blogs/index.htm', locals())

def blog(request, urlblog):
    try:
        blog = Blog.objects.get(url=urlblog)
        return render_to_response('blogs/blog_index.htm', locals())
    except:
        blogs = Blog.objects.all()
        num_blogs = len(blogs)
        host = HOST.strip("/")
        return render_to_response('blogs/blog_inexistente.htm', locals())

