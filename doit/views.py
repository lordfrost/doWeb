# -*- coding: utf-8 -*-
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Здравствуй, мир")

def DateTimeNow(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def TimePlus(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)