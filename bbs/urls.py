from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='bbs.home'),
    url(r'^(?P<thread_id>\d+)/$', views.show_thread, name='bbs.thread.show'),

    url(r'^add/$', views.edit_thread, name='bbs.thread.add'),
    url(r'^edit/(?P<thread_id>\d+)/$', views.edit_thread, name='bbs.thread.edit'),
    url(r'^delete/(?P<thread_id>\d+)/$', views.delete_thread, name='bbs.thread.delete'),

    url(r'^(?P<thread_id>\d+)/comment/edit/(?P<comment_id>\d+)/$', views.edit_comment, name='bbs.comment.edit'),
    url(r'^(?P<thread_id>\d+)/comment/delete/(?P<comment_id>\d+)/$', views.delete_comment, name='bbs.comment.delete'),

)