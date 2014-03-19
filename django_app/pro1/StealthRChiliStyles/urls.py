from django.conf.urls import patterns, include, url
from MusicApp.views import my_homepage_view, musicSet, homepage
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', my_homepage_view),
    url(r'^locM$', 'MusicApp.views.ajax6'),
    url(r'^locMus$', 'MusicApp.views.ajax5'),
    url(r'^locMusic$', 'MusicApp.views.ajax4'),
    url(r'^locMusic_json$', 'MusicApp.views.ajax3'),
    url(r'^music_set$', 'MusicApp.views.ajax2'),
    url(r'^homepage/', homepage),
    url(r'^musicSet/', musicSet)
)
