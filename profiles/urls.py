from django.urls import re_path
from .views import ProfileDetailView, RandomProfileDetailView

app_name='profiles'
urlpatterns = [
    re_path(r'^random/$', RandomProfileDetailView.as_view(), name='random'),
    re_path(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]
