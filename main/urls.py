from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views
'''
Order of Completion:
X   Base Template
X   Feed (only using base template)
X   RegistrationView
X   UserPostsView (sidebar only)
X   SignInView
X   CreateCommunityView
X   CommunityListView (list only)
X   CommunityView (sidebar only)
X   Create Post View
X   Thread View (root post only)
    UserPostsView
    Feed View (populate by most recent, anywhere)
    UserCommunitiesView
    Thread View (with comments)
    Reply View
    Community View
    CommunityListView (community following)
    FeedView (population based on followed communities)
    Style everything!
'''

urlpatterns = [
    path("feed", views.FeedView, name="feed"),
    # community and post-related views
    path("r/<str:name>", views.CommunityView, name="community"),
    path("r-list", views.CommunityListView, name="communitylist"),
    path("new-community", views.CreateCommunityView, name="createcommunity"),
    path("new-thread", views.CreatePostView, name="newthread"),
    path("r/<str:community>/new-thread", views.CreatePostView, name="newthread"),
    path("r/<str:community>/thread/<int:thread_pk>", views.ThreadView, name="thread"),
    path("r/<str:community>/thread/<int:thread_pk>/<int:post_pk>", views.ThreadView, name="thread"),

    # user related views
    path("signin", views.SignInView, name="signin"),
    path("register", views.RegisterView, name="register"),
    path(
        "u/<str:username>/posts",
        views.UserPostsView,
        name="userposts"
    ),
    path(
        "u/str:username/communities",
        views.UserCommunitiesView,
        name="usercommunities",
    ),
    path("logout", views.LogoutView, name="logout"),

    # convenient redirects
    path("", RedirectView.as_view(pattern_name="feed")),
]
