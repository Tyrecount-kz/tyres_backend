from .views import ShopUserListView, ShopUserRUDView,ShopUserPostsListView

from django.urls import path,re_path

urlpatterns = [
    re_path(r'^$', ShopUserListView.as_view(), name='user-list'),
    re_path(r'^(?P<pk>\d+)/$', ShopUserRUDView.as_view(), name='user-detail'),
    re_path(r'^(?P<pk>\d+)/posts/$', ShopUserPostsListView.as_view(), name='user-posts')
]
