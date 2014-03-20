from django import http
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def mail(request):
    if request.method == 'POST':
        return http.HttpResponse('frate1839@gmail.com', mimetype='text/plain')
    else:
        return http.HttpResponse('endaaman', mimetype='text/plain')
