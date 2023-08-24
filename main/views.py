from django.core.paginator import Paginator
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth import login, authenticate
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from . import models
from . import forms

# Create your views here.

def FeedView(request, page):
    posts = models.Post.objects.all()
    context = {
        # TODO
    }
    return render(request, template_name="feed.html", context=context)

def CommunityView(request, name, page):
    community = models.Community.objects.get(name=name)
    posts = community.post_set.all()
    post_page = Paginator(posts, 10).get_page(page)
    
    context = {
        "posts": post_page,
        "pagenum": page,
        "name": community.name,
    }
    return render(request, template_name="community.html", context=context)

def CreatePostView(request, community): 
    raise Http404

def ReplyView(request, community, pk, page):
    raise Http404

def RegistrationView(request):
    raise Http404

def SignInView(request):
    if (request.method == "GET"):
        form = forms.SignInForm
    elif (request.method == "POST"):
        pass
    else:
        raise SuspiciousOperation


def ThreadView(request, community, pk, page):
    mainpost = models.MainPost.objects.get(pk=pk)
    context = {
        "mainpost": mainpost,
    }
    return render(request, template_name="thread.html", context=context)

def UserPostsView(request, username, page):
    context = {
        "userdata": models.UserData.objects.get(username=username)
    }
    raise Http404

def UserCommunitiesView(request, username, page):
    raise Http404