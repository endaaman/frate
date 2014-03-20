from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^mail/$', views.mail, name='ajax.mail'),
)