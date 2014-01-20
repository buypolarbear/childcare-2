from django.conf.urls import patterns, url, include
from rest_framework import routers
from childcare.apps.progress.views import ActivityViewSet

__author__ = 'angelo'


router = routers.DefaultRouter()
router.register(r'activities', ActivityViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls))
)