from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^login/$', views.login, name='auth.login'),
    url(r'^logout/$', views.logout, name='auth.logout'),
)
