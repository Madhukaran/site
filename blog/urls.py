from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostShareView
)
from .feeds import LatestPostsFeed
from .views import robots

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', PostListView.as_view(),
         name='post_list_by_tag'),
    path(' <slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('robots.txt/', robots, name='robots.txt'),
    path('<int:post_id>/share/', PostShareView.as_view(), name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
