from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from photo.models import Album, Photo


@csrf_protect
def home(request):
    return render_to_response('home.html',
                              dict(albums=Album.objects.all(), photos=Photo.objects.all()),
                              context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))

