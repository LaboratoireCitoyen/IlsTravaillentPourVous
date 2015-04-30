from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HomeView, AutocompleteView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^autocomplete/$', AutocompleteView.as_view(),
        name='autocomplete'),

    url(r'^deputes/', include('francedata.deputes.urls')),
    url(r'^votes/', include('francedata.votes.urls')),

    url(r'^pirate/', include(admin.site.urls)),
)
