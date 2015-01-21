from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static

import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^album/', include('apps.photo.urls')),
    url(r'^member/', include('apps.member.urls')),
    url(r'^bbs/', include('apps.bbs.urls')),
    url(r'^auth/', include('apps.auth.urls')),
    url(r'^blog/', include('apps.blog.urls')),

    url(r'^mail$', views.mail, name='mail'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
