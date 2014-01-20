__author__ = 'angelo'
from django.conf.urls import patterns, url
from childcare.apps.webapp.views import HomePage

urlpatterns = patterns('',
    url('^accounts/login', 'django.contrib.auth.views.login'),
    url(r'^children', HomePage.as_view())
)