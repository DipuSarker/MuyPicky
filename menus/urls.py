from django.urls import re_path

from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
)

app_name='menus'
urlpatterns = [
    re_path(r'^create/$',  ItemCreateView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    re_path(r'$', ItemListView.as_view(), name='list'),
]
