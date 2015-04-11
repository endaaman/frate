from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='album.home'),
    url(r'^add/$', views.edit_album, name='album.add'),
    url(r'^(?P<album_id>\d+)/$', views.show_album, name='album.show'),
    url(r'^(?P<album_id>\d+)/edit/$', views.edit_album, name='album.edit'),
    url(r'^(?P<album_id>\d+)/delete/$', views.delete_album, name='album.delete'),

    url(r'^(?P<album_id>\d+)/photo/add/$', views.edit_photo, name='photo.add'),
    url(r'^(?P<album_id>\d+)/photo/(?P<photo_id>\d+)/edit/$', views.edit_photo, name='photo.edit'),
    url(r'^(?P<album_id>\d+)/photo/(?P<photo_id>\d+)/delete/$', views.delete_photo, name='photo.delete'),
)
