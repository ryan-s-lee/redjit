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
    CommunityView (sidebar only)
    Create Post View
    UserPostsView
    CommunityListView (community following)
    Feed View (complete)
    UserCommunitiesView
    Thread View
    Reply View
    Community View
    Style everything!
'''

urlpatterns = [
    path("feed", views.FeedView, name="feed"),
    # community and post-related views
    path("r/<str:name>", views.CommunityView, name="community"),
    path("r-list", views.CommunityListView, name="communitylist"),
    path("create-community", views.CreateCommunityView, name="createcommunity"),
    path("r/<str:community>/post", views.CreatePostView, name="createpost"),

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
