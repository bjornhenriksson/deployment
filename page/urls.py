from django.conf.urls import patterns, url

from page import views

urlpatterns = patterns('',
    url(r'^$', views.header, name='header'),
)