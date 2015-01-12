from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HomeView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^deputes/', include('deputes.urls')),

    url(r'^pirate/', include(admin.site.urls)),
)
