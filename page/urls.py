from django.conf.urls import patterns, url

from page import views

urlpatterns = patterns('',
    url(r'^(?P<page>\w+)/$', views.post, name='post'),
    url(r'^(?P<page>\w+)/edit/(?P<post>\w+)/$', views.edit, name='edit'),
)