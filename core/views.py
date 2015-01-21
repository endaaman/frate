from django import http
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))


@csrf_exempt
def mail(request):
    if request.method == 'POST':
        return http.HttpResponse('frate1839@gmail.com', content_type='text/plain')
    else:
        return http.HttpResponse('endaaman', content_type='text/plain')
