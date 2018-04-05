from django.shortcuts import render, render_to_response
from contactUs.models import Feedback


def contactUs(request):
    return render(request, 'contactUs.html')

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
