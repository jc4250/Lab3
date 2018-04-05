from django.shortcuts import render
from django.template.context_processors import csrf
from .models import Feedback


def contact(request):
    return render(request, 'contactUs.html')

def about(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'contact.html', c)

def feedback(request):
    email = request.POST.get('email', '')
    feedback = request.POST.get('feedback', '')
    for i in Feedback.objects.all():
        if email == i.email:
            return render(request, 'home.html')
    q = Feedback(
        email=email,
        feedback=feedback,
    )
    q.save()
    return render(request, 'home.html')
