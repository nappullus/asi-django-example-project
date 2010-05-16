from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post

def index(request):
    posts = Post.objects.all()
    return render_to_response("blog/index.html",
        {'posts': posts},
        context_instance=RequestContext(request))
