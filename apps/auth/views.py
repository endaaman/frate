from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    form = AuthenticationForm(data=request.POST)
    if request.POST:
        if form.is_valid:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                nxt = request.POST.get('next', '/')
                return HttpResponseRedirect(nxt)
            else:
                pass
                # invalid account

    nxt = request.GET.get('next', '/')

    return render(
        request,
        'auth/login.html',
        dict(
            form=form,
            next=nxt,
        ),
        context_instance=RequestContext(request)
    )


def logout(request):
    if request.POST:
        nxt = request.POST.get('next', '/')
    elif request.GET:
        nxt = request.GET.get('next', '/')
    else:
        nxt = '/'

    auth.logout(request)
    return HttpResponseRedirect(nxt)
