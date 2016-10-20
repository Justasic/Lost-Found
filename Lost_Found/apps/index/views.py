from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from Lost_Found.apps.index.models import Item, Note, PhoneNumber
from django.db.models import Q

# Create your views here.

# This view shows the overview page for all items currently in lost and found.
def overview(request):

    items = Item.objects.filter(Q(istatus='S') | Q(istatus='L'))
    ctx = RequestContext(request, {
        'items': items,
    })

    return render_to_response('index/index.html', ctx)

# this view is what handles the aging auditing of the lost and found system.
# Viewing this page will show all lost items greater than the set legal timeframe.
# (example, oregon state has a 60 day wait period before you can dispose of the items, this shows
# all items older than 60 days.)
def aging(request):

    ctx = RequestContext(request, {'None': None})
    return render_to_response('index/aging.html', ctx)

def printable(request, docid):
    pass
