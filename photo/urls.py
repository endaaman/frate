from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='album.home'),
    url(r'^add/$', views.edit_album, name='album.add'),
    url(r'^(?P<album_id>\d+)/$', views.show_album, name='album.show'),
    url(r'^edit/(?P<album_id>\d+)/$', views.edit_album, name='album.edit'),
    url(r'^delete/(?P<album_id>\d+)/$', views.delete_album, name='album.delete'),

    url(r'^(?P<album_id>\d+)/photo/add/$', views.edit_photo, name='photo.add'),
    url(r'^(?P<album_id>\d+)/photo/edit/(?P<photo_id>\d+)/$', views.edit_photo, name='photo.edit'),
    url(r'^(?P<album_id>\d+)/photo/delete/(?P<photo_id>\d+)/$', views.delete_photo, name='photo.delete'),

    url(r'bg/$', views.get_bg, name='photo.bg'),
)
