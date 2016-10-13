from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

# Create your views here.

def overview(request):

    ctx = RequestContext(request, {'None': None})

    return render_to_response('index/index.html')


def aging(request):

    ctx = RequestContext(request, {'None': None})
    return render_to_response('index/aging.html')
