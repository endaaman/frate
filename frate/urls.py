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

    url(r'^album/', include('photo.urls')),
    url(r'^member/', include('member.urls')),
    url(r'^bbs/', include('bbs.urls')),
    url(r'^auth/', include('auth.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^ajax/mail/$', views.mail, name='ajax.mail'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
