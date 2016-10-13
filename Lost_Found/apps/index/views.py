from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

# Create your views here.

# This view shows the overview page for all items currently in lost and found.
def overview(request):

    ctx = RequestContext(request, {'None': None})

    return render_to_response('index/index.html')

# this view is what handles the aging auditing of the lost and found system.
# Viewing this page will show all lost items greater than the set legal timeframe.
# (example, oregon state has a 60 day wait period before you can dispose of the items, this shows
# all items older than 60 days.)
def aging(request):

    ctx = RequestContext(request, {'None': None})
    return render_to_response('index/aging.html')

def printable(request, docid):
    pass
