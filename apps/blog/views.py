#-*-encoding:utf-8-*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django import http
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from models import *
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.core.urlresolvers import reverse
import json


class UrlNameError(forms.ValidationError):
    def __init__(self):
        return forms.ValidationError.__init__(self, 'This name is already allocated.')


class BlogForm(forms.ModelForm):

    def clear_name(self):
        base = self.data.get('url_name', None)
        if base:
            b = Blog.objects.filter(url_name=base)
            if len(b) > 0:
                raise UrlNameError()
        return base

    class Meta:
        model = Blog
        fields = ('title', 'author', 'message', 'url_name', )
        help_texts = {
            'message': '本文には<a href="%s" target="_blank">Markdown記法</a>が使えます。' % '/blog/markdown/',
            'url_name': 'URLに使われる名前です。「test」の場合はhttp:/frate.tk/blog/test/が記事のURLになります。',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'message', 'edit_key', )


def home(request):
    return render_to_response(
        'blog/home.html',
        dict(
            blogs=Blog.objects.order_by('-pub_date'),
        ),
        context_instance=RequestContext(request)
    )


def show_blog(request, blog_name):
    try:
        blog = Blog.objects.get(url_name=blog_name)
    except Blog.DoesNotExist:
        return http.HttpResponseNotFound()

    if request.method == 'POST':
        comment = Comment()
        comment.blog_id = blog.id
        comment_form = CommentForm(request.POST, instance=comment)
        v = comment_form.is_valid()
        if v:
            comment_form.save()

        ajax = request.GET.get('use-ajax', None)
        if ajax != 'true':
            # ajaxでない
            if v:
                # validならリダイレクト
                return http.HttpResponseRedirect(reverse('blog.show', args=(blog_name,)))
            else:
                # invalidなら下で処理
                context = request.POST
        else:
            # ajaxなときvalid,invalid問わず
            import json
            content = dict(result=v, errors=comment_form.errors, redirect_to=reverse('blog.show', args=(blog_name,)))
            return http.HttpResponse(json.dumps(content), mimetype='text/plain')

    else:
        context = {}
        comment_form = CommentForm()
        comment_form.blog = blog.id


    return render(
        request,
        'blog/show_blog.html',
        dict(
            blog=blog,
            comments=blog.comment_set.all(),
            comment_form=comment_form,
        ),
        context_instance=RequestContext(request, context)
    )



@user_passes_test(lambda u: u.has_module_perms('blog'))
def edit_blog(request, blog_name=None):

    if blog_name is None:
        blog = Blog()
    else:
        blog = get_object_or_404(Blog, url_name=blog_name)

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=blog)
        v = blog_form.is_valid()
        if v:
            blog = blog_form.save()
            blog_name = blog.url_name

        ajax = request.GET.get('use-ajax', None)
        if ajax != 'true':
            # ajaxでない
            if v:
                # validならリダイレクト
                return http.HttpResponseRedirect(reverse('blog.show', args=(blog_name,)))
            else:
                # invalidなら下で処理
                context = request.POST
        else:
            # ajaxなときvalid,invalid問わず
            import json
            content = dict(result=v, errors=blog_form.errors, redirect_to=reverse('blog.show', args=(blog_name,)))
            return http.HttpResponse(json.dumps(content), mimetype='text/plain')

    else:
        context = {}
        blog_form = BlogForm(instance=blog)

    return render_to_response('blog/edit_blog.html',
                              dict(
                                  blog=blog,
                                  blog_form=blog_form,
                              ),
                              context_instance=RequestContext(request, context))



@user_passes_test(lambda u: u.has_module_perms('blog'))
def delete_blog(request, blog_name):
    blog = get_object_or_404(Blog, url_name=blog_name)

    if request.method == 'POST':
        blog.delete()
        ajax = request.GET.get('use-ajax', None)
        if ajax == 'true':
            content = dict(result=True, errors={}, redirect_to=reverse('blog.home'))
            return http.HttpResponse(json.dumps(content), mimetype='text/plain')
        else:
            return http.HttpResponseRedirect(reverse('blog.home'))
    else:
        return http.HttpResponseForbidden()
