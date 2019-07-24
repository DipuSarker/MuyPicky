from django.urls import re_path

from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView

)

app_name='restaurants'
urlpatterns = [
    re_path(r'^create/$',  RestaurantCreateView.as_view(), name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),
    re_path(r'$', RestaurantListView.as_view(), name='list'),
]
