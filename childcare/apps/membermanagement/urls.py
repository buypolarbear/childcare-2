from django.conf.urls import patterns, url, include
from rest_framework import routers
from views import StudentViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'guardians', UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls))
)