from django.core.paginator import Paginator
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from . import models
from . import forms

# Create your views here.


def FeedView(request):
    context = {
        "posts": models.Thread.objects.all(),
    }
    return render(request, template_name="feed.html", context=context)


def CreatePostView(request, community):
    raise Http404


def CreateCommunityView(request):
    if not request.user.is_authenticated:
        return redirect("signin")

    if request.method == "GET":
        form = forms.CreateCommunityForm()
    elif request.method == "POST":
        form = forms.CreateCommunityForm(request.POST)
        if form.is_valid():
            community = form.save()
            request.user.userdata.communities.add(community)
            request.user.userdata.moderating.add(community)
            return redirect("community", name=community.name)
    else:
        raise SuspiciousOperation

    context = {"form": form}
    return render(request, template_name="createcommunity.html", context=context)


def CommunityView(request, name):
    community = models.Community.objects.get(name=name)
    threads= community.thread_set.all()
    if "page" in request:
        pagenum = request.GET["page"]
    else:
        pagenum = 1
    threads_page = Paginator(threads, 10).get_page(pagenum)

    context = {
        "threads": threads_page,
        "pagenum": pagenum,
        "community": community,
    }
    return render(request, template_name="community.html", context=context)


def CommunityListView(request):
    if request.method == "GET":
        communities = models.Community.objects.all()
        context = {
            "communities": communities,
        }
        return render(request, template_name="communitylist.html", context=context)
    elif request.method == "POST":
        # communities_to_join = [
        #     communityname
        #     for communityname in request.POST
        #     if communityname != "csrfmiddlewaretoken"
        # ]
        # for community in communities_to_join:
        #     # communities to remove is the difference of user's communities
        #     # and form-submitted communities
        return redirect("feed")


def LogoutView(request):
    logout(request)
    return redirect("feed")


def ReplyView(request, community, pk, page):
    raise Http404


def RegisterView(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():  # let form validation take care of username check
            loginfo = form.cleaned_data
            userdata = models.UserData.objects.create_user(
                loginfo["username"],
                loginfo["email"],
                loginfo["password"],
            )
            login(request, userdata.user)
            return redirect("feeddefault")
    elif request.method == "GET":
        form = forms.RegistrationForm()

    return render(
        request,
        template_name="register.html",
        context={
            "form": form,
        },
    )


def SignInView(request):
    if request.user.is_authenticated:
        print("User already authenticated, redirecting to feed")
        return redirect("feed")

    if request.method == "GET":
        form = forms.SignInForm()
    elif request.method == "POST":
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("feed")
    else:
        raise SuspiciousOperation

    return render(request, template_name="signin.html", context={"form": form})


def ThreadView(request, community, pk):
    mainpost = models.Thread.objects.get(pk=pk)
    context = {
        "mainpost": mainpost,
    }
    return render(request, template_name="thread.html", context=context)


def UserPostsView(request, username, page=1):
    userdata = models.User.objects.get(username__exact=username).userdata
    communities = userdata.communities.all()
    context = {
        "userdata": userdata,
        "communities": communities,
    }
    return render(request, template_name="userposts.html", context=context)


def UserCommunitiesView(request, username, page):
    raise Http404
