from django.urls import re_path, path, include
from django.contrib import admin
from django.views.generic import TemplateView


from django.contrib.auth.views import LoginView, LogoutView

from menus.views import HomeView, AllUserRecentItemListView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^recent/$', AllUserRecentItemListView.as_view(), name='recent'),
    re_path(r'^register/$', RegisterView.as_view(), name='register'),
    re_path(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    re_path(r'^u/', include('profiles.urls')),
    re_path(r'^items/', include('menus.urls')),
    re_path(r'^restaurants/', include('restaurants.urls')),
    re_path(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    re_path(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
