from django.conf.urls import patterns, url

from page import views

urlpatterns = patterns('',
    url(r'^(?P<page>\w+)/$', views.post, name='post'),
)