# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Здравствуй, мир")

def DateTimeNow(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def TimePlus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>It is now %s and will be %s.</body></html>" % (now, offset)
    return HttpResponse(html)