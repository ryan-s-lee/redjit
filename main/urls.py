from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('/thread', views.ThreadView),
    path('/feed', views.FeedView),
    path('', RedirectView.as_view(url="/main/feed")),
]