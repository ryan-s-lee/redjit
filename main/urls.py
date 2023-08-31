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
X   UserPostsView
X   Feed View (populate by most recent, anywhere)
X   UserCommunitiesView
    Thread View (with comments)
    Reply View
X   Community View
X   CommunityListView (community following)
    FeedView (population based on followed communities)
    Style everything!
    Add a search bar in feed for looking up communities, posts, and users
    Add a search bar in communities for looking up posts specific to the community
    Add a search bar in users for looking up communities and posts related to a user
    Add a search bar in threads for looking up relevant posts within the thread
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
    path("r/<str:community>/thread/<int:thread_pk>/<int:post_pk>", views.ThreadView, name="thread_post"),

    # user related views
    path("signin", views.SignInView, name="signin"),
    path("register", views.RegisterView, name="register"),
    path(
        "u/<str:username>/posts",
        views.UserPostsView,
        name="userposts"
    ),
    path(
        "u/<str:username>/communities",
        views.UserCommunitiesView,
        name="usercommunities",
    ),
    path("logout", views.LogoutView, name="logout"),

    # convenient redirects
    path("", RedirectView.as_view(pattern_name="feed")),
]
