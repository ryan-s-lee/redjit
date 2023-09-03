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
        "threads": models.Thread.objects.all(),
    }
    return render(request, template_name="feed.html", context=context)


def CreatePostView(request, community=None):
    context = {}
    if not request.user.is_authenticated:
        return redirect("signin")

    if request.method == "GET":
        prerecorded_data = {"community": community}

        context["thread_form"] = forms.NewThreadForm(
            prerecorded_data, prefix="thread-data"
        )
        context["post_form"] = forms.NewPostForm(prefix="post-content")
    elif request.method == "POST":
        print(request.POST)
        form1 = forms.NewThreadForm(request.POST, prefix="thread-data")
        form2 = forms.NewPostForm(request.POST, prefix="post-content")

        if form1.is_valid() and form2.is_valid():
            post = models.Post(
                content=form2["content"].value(),
                author=request.user.userdata,
                parent=None,
            )
            post.save()

            submitted_community = models.Community.objects.get(
                pk=form1["community"].value()
            )
            thread = models.Thread.objects.create(
                title=form1["title"].value(),
                root_post=post,
                community=submitted_community,
            )
            return redirect(
                "thread", community=submitted_community, thread_pk=thread.pk
            )
        else:
            context["thread_form"] = form1
            context["post_form"] = form2
    else:
        raise SuspiciousOperation

    return render(request, template_name="createpost.html", context=context)


def CreateCommunityView(request):
    if not request.user.is_authenticated:
        return redirect("signin")

    if request.method == "GET":
        form = forms.CreateCommunityForm()
    elif request.method == "POST":
        form = forms.CreateCommunityForm(request.POST)
        if form.is_valid():
            community = form.save()
            if hasattr(request.user, "userdata"):
                request.user.userdata.communities.add(community)
                request.user.userdata.moderating.add(community)

            return redirect("community", name=community.name)
    else:
        raise SuspiciousOperation

    context = {"form": form}
    return render(request, template_name="createcommunity.html", context=context)


def CommunityView(request, name):
    community = models.Community.objects.get(name=name)
    threads = community.thread_set.all()
    if "page" in request.GET:
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


def ReplyView(request, community, post_pk):
    if not request.user.is_authenticated:
        return redirect("signi")

    toReplyTo = models.Post.objects.get(pk=post_pk)
    curpost = toReplyTo
    replychain = [curpost]
    while curpost.parent is not None:
        curpost = curpost.parent
        replychain.insert(0, curpost)
    if request.method == "GET":
        replyform = forms.ReplyForm(request.POST)
    elif request.method == "POST":
        replyform = forms.ReplyForm(request.POST)
        if replyform.is_valid():
            models.Post.objects.create(
                author=request.user.userdata,
                content=replyform["content"].value(),
                parent=toReplyTo
            )
            return redirect("thread", community=community, thread_pk=replychain[0].thread.pk)
    else:
        raise SuspiciousOperation

    return render(request, template_name="reply.html", context={
        "replychain": replychain,
        "replyform": replyform,
    })



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
            return redirect("feed")
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


def ThreadView(request, community, thread_pk, post_pk=None):
    context = {}
    context["thread"] = models.Thread.objects.get(pk=thread_pk)
    if (post_pk is not None):
        context["post"] = models.Post.objects.get(pk=post_pk)
        context["replies"] = context["post"].replies.all()
    else:
        context["replies"] = context["thread"].root_post.replies.all()



    return render(request, template_name="thread.html", context=context)


def UserPostsView(request, username, page=1):
    userdata = models.User.objects.get(username__exact=username).userdata
    communities = userdata.communities.all()

    # TODO: get a list of threads where each thread contains a post in userdata
    def get_thread(post):
        curpost = post
        while curpost.parent is not None:
            curpost = curpost.parent
        return curpost.thread

    thread_post_pairs = [(get_thread(post), post) for post in userdata.post_set.all()]

    context = {
        "viewed_userdata": userdata,
        "communities": communities,
        "thread_post_pairs": thread_post_pairs,
    }
    return render(request, template_name="userposts.html", context=context)


def UserCommunitiesView(request, username):
    context = {}
    viewed_userdata = models.User.objects.get(username=username).userdata
    context["viewed_userdata"] = viewed_userdata
    context["communities"] = viewed_userdata.communities.all()
    return render(request, template_name="usercommunities.html", context=context)
