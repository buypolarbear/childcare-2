from django.contrib import admin
from django.conf.urls import patterns, include, url


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
from startproject import apps

admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #webapp
    url(r'^', include('apps.webapp.urls')),

    #api
    url(r'^api/membermanagement/', include('apps.membermanagement.urls')),
    url(r'^api/progress/', include('apps.progress.urls'))
)
