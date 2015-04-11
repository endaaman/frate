from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='blog.home'),

    url(r'^add/$', views.edit_blog, name='blog.add'),
    url(r'^edit/(?P<blog_name>\S+)/$', views.edit_blog, name='blog.edit'),
    url(r'^delete/(?P<blog_name>\S+)/$', views.delete_blog, name='blog.delete'),
    url(r'^(?P<blog_name>\S+)/$', views.show_blog, name='blog.show'),
    # url(r'^(?P<blog_id>\d+)/comment/^(?P<blog_id>\d+)/edit/$', views.show_blog, name='blog.edit_comment'),
    # url(r'^(?P<blog_id>\d+)/comment/^(?P<blog_id>\d+)/delete/$', views.show_blog, name='blog.delete_comment'),

)
