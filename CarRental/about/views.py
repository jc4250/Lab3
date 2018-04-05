from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf

def about(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'contact.html', c)