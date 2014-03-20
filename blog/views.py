#-*-encoding:utf-8-*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django import http
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from models import *
from abstract.views import MessageBaseForm
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.core.urlresolvers import reverse


class UrlNameError(forms.ValidationError):
    def __init__(self):
        return forms.ValidationError.__init__(self, 'This name is already allocated.')


class BlogForm(MessageBaseForm):

    def clear_name(self):
        base = self.data.get('url_name', None)
        if base:
            b = Blog.objects.filter(url_name=base)
            if len(b) > 0:
                raise UrlNameError()
        return base

    class Meta(MessageBaseForm.Meta):
        model = Blog
        def __init__(self):
            self.help_texts['url_name'] = 'URLに使われる名前です。「test」の場合はhttp:/frate.tk/blog/test/が記事のURLになります。'


class CommentForm(MessageBaseForm):
    class Meta(MessageBaseForm.Meta):
        model = Comment
        exclude = ('blog', ) + MessageBaseForm.Meta.exclude




def home(request):
    return render_to_response(
        'blog/home.html',
        dict(
            blogs=Blog.objects.order_by('-pub_date'),
        ),
        context_instance=RequestContext(request)
    )

@csrf_protect
def show_blog(request, blog_name):
    try:
        blog = Blog.objects.get(url_name=blog_name)
    except Blog.DoesNotExist:
        return http.HttpResponseNotFound()

    if request.POST:
        comment = Comment()
        comment.blog_id = blog.id
        comment_form = CommentForm(request.POST, instance=comment)
        v = comment_form.is_valid()
        if v:
            comment_form.save()

        v_flag = request.GET.get('validation', None)
        if v_flag != 'true':
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


@csrf_protect
@user_passes_test(lambda u: u.has_module_perms('blog'))
def edit_blog(request, blog_name=None):

    if blog_name is None:
        blog = Blog()
    else:
        blog = get_object_or_404(Blog, url_name=blog_name)

    if request.POST:
        blog_form = BlogForm(request.POST, instance=blog)
        v = blog_form.is_valid()
        if v:
            blog = blog_form.save()
            blog_name = blog.url_name

        v_flag = request.GET.get('validation', None)
        if v_flag != 'true':
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


@csrf_protect
@user_passes_test(lambda u: u.has_module_perms('blog'))
def delete_blog(request, blog_name):
    blog = get_object_or_404(Blog, url_name=blog_name)
    if request.POST:
        blog.delete()
        return http.HttpResponseRedirect(reverse('blog.home'))
    else:
        return http.HttpResponseForbidden()
