from Monitoring.urls import urlpatterns
from django.contrib import admin
admin.autodiscover()
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from Monitoring.urls import urlpatterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'Monitoring.views.index', name='index'),
    url(r'^admin', include(admin.site.urls)),
    url(r'^', include('Monitoring.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


