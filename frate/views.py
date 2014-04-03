from django import http
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from photo.models import Album, Photo


def home(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))



@csrf_exempt
def mail(request):
    if request.method == 'POST':
        return http.HttpResponse('frate1839@gmail.com', mimetype='text/plain')
    else:
        return http.HttpResponse('endaaman', mimetype='text/plain')
