# coding: utf-8
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
    return render_to_response('main.html', locals())


def login_form(request):
    args = {}
    args.update(csrf(request))
    args['next'] = request.GET.get('next')
    return render_to_response('login.html', args)


def register(request):
    next = request.GET.get('next')

    user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))

    if user is not None:
        login(request, user)

    return HttpResponseRedirect(next)


def log_out(request):
    logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])