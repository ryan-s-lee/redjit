from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views
'''
Order of Completion:
X   Base Template
X   Feed (only using base template)
X   RegistrationView
    UserPostsView (sidebar only)
X   SignInView
    CreateCommunityView
    CommunityView (sidebar only)
    Create Post View
    Feed View (complete)
    UserPostsView
    UserCommunitiesView
    Thread View
    Reply View
    Community View
    Style everything!
'''

urlpatterns = [
    path("feed", views.FeedView, name="feed"),
    path("feed/<int:page>", views.FeedView, name="feed"),
    # community and post-related views
    path("r/<str:name>/page_<int:page>", views.CommunityView, name="community"),
    path("create-community", views.CreateCommunityView, name="createcommunity"),
    path("r/<str:community>/main_<int:mainpostkey>/<int:pk>/page_<int:page>", views.ThreadView, name="viewthread"),
    path("r/<str:community>/post", views.CreatePostView, name="createpost"),
    path("r/<str:community>/reply/to<int:pk>/page<int:page>", views.ReplyView, name="reply"),

    # user related views
    path("signin", views.SignInView, name="signin"),
    path("register", views.RegisterView, name="register"),
    path(
        "u/<str:username>/posts/<int:page>",
        views.UserPostsView,
        name="userposts",
    ),
    path(
        "u/<str:username>/communities/<int:page>",
        views.UserCommunitiesView,
        name="usercommunities",
    ),
    path("logout", views.LogoutView, name="logout"),

    # convenient redirects
    path("", RedirectView.as_view(pattern_name="feed")),
]
