from django.shortcuts import render, render_to_response
from django.template import RequestContext

def test(request):
    return render_to_response('test.html',
        context_instance=RequestContext(request))
