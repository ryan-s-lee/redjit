from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views
'''
Order of Completion:
1. Base Template
2. Feed (only using base template)
3. Registration View
4. Sign In View
5. Create Community View
6. Create Post View
7. Feed View (complete)
8. UserPostsView
9. UserCommunitiesView
10. Thread View
11. Reply View
12. Community View
'''

urlpatterns = [
    path("feed/<int:page>", views.FeedView, name="feed"),
    # community and post-related views
    path("r/<str:name>/<int:page>", views.CommunityView, name="community"),
    path("create-community", views.CreateCommunityView, name="createcommunity"),
    path("r/<str:community>/<int:mainpostkey><int:pk>/<int:page>", views.ThreadView, name="viewthread"),
    path("r/<str:community>/post", views.CreatePostView, name="createpost"),
    path("r/<str:community>/reply/<int:pk>/<int:page>", views.ReplyView, name="reply"),

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

    # convenient redirects
    path("", RedirectView.as_view(pattern_name="feed")),
]
