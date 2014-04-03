from django.conf.urls import patterns, include, url

from django.contrib import admin
import settings

import views

admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'frate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(django.contrib.admin.urls)),

    url(r'^album/', include('photo.urls')),
    url(r'^member/', include('member.urls')),
    url(r'^bbs/', include('bbs.urls')),
    url(r'^auth/', include('auth.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^ajax/mail/$', views.mail, name='ajax.mail'),
)

urlpatterns += patterns('django.views.static',
    (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    (r'static/(?P<path>.*)', 'serve', {'document_root': settings.STATIC_ROOT}),
)

