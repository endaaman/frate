#-*- encoding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from django import http
from models import *
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import json


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ('album', )


def get_bg(request):
    albums=Album.objects.all()

    # other = Album.get_other_album()
    ps = Photo.objects.filter(album__isnull=True)
    for p in ps:
        p.album_id = 1
    # albums.apped(other)
    return http.HttpResponse('frate1839@gmail.com', content_type='text/plain')


def home(request):
    albums = Album.objects.order_by('-pub_date')

    return render_to_response('photo/home.html',
                              dict(
                                  albums=albums,
                              ),
                              context_instance=RequestContext(request))



@login_required(redirect_field_name='next')
def edit_album(request, album_id=None):

    if album_id is None:
        album = None
        op = '追加'
    else:
        album = get_object_or_404(Album, pk=album_id)
        op = '編集'

    context = {}
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album)
        v = album_form.is_valid()
        if v:
            album = album_form.save()
            album_id = album.id

            if request.is_ajax():
                content = dict(result=v, errors=album_form.errors, redirect_to=reverse('album.show', args=(album_id,)))
                import json
                return http.HttpResponse(json.dumps(content), content_type='text/plain')
            else:
                return http.HttpResponseRedirect(reverse('album.show', args=(album_id,)) )
        else:
            context = request.POST

    else:
        album_form = AlbumForm(instance=album)

    return render_to_response('photo/edit_album.html',
                              dict(
                                  album_form=album_form,
                                  album=album,
                                  op=op,
                              ),
                              context_instance=RequestContext(request, context))





def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        album.delete()
        if request.is_ajax():
            content = dict(result=True, errors={}, redirect_to=reverse('album.home'))
            return http.HttpResponse(json.dumps(content), content_type='text/plain')
        else:
            return http.HttpResponseRedirect(reverse('album.home'))
    else:
        return http.HttpResponseNotFound()



def show_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render_to_response('photo/show_album.html',
                              dict(
                                  album=album,
                                  photos=album.photo_set.all()
                              ),
                              context_instance=RequestContext(request, {}))




def edit_photo(request, album_id=None, photo_id=None):
    if not album_id is None:
        album = get_object_or_404(Album, pk=album_id)

    if photo_id is None:
        photo = Photo()
        op = u'追加'
    else:
        photo = get_object_or_404(Photo, pk=photo_id)
        op = u'編集'

    photo.album_id = album_id

    context = {}

    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES, instance=photo)
        v = photo_form.is_valid()
        if v:
            photo_form.save()

            if request.is_ajax():
                content = dict(result=v, errors=photo_form.errors, redirect_to=reverse('album.show', args=(album_id,)))
                return http.HttpResponse(json.dumps(content), content_type='text/plain')
            else:
                return http.HttpResponseRedirect(reverse('album.show', args=(album_id,)))
            # ajaxでない
        else:
            context = request.POST

    else:
        photo_form = PhotoForm(instance=photo)

    return render_to_response('photo/edit_photo.html',
                              dict(
                                  photo=photo,
                                  photo_form=photo_form,
                                  album_id=album_id,
                                  op=op,
                              ),
                              context_instance=RequestContext(request, context))





def delete_photo(request, album_id, photo_id):
    get_object_or_404(Album, pk=album_id)
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        photo.delete()
        if request.is_ajax():
            content = dict(result=True, errors={}, redirect_to=reverse('album.show', args=(album_id, )))
            return http.HttpResponse(json.dumps(content), content_type='text/plain')
        else:
            return http.HttpResponseRedirect(reverse('album.show', args=(album_id,)))
    else:
        return http.HttpResponseNotFound()


