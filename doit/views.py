# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime


def hello(request):
    return HttpResponse("Здравствуй, мир")


def DateTimeNow(request):
    now = datetime.datetime.now()
    return render_to_response('time.html', {'now': now})


def TimePlus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now_plus_url = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('timeplus.html', {'now': datetime.datetime.now, 'nowplus': now_plus_url,
                                                'raznica': offset})