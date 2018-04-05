from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from .models import register
from django.http import HttpResponse, HttpResponseRedirect


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def verification(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    for i in register.objects.all():
        if username==i.username and password==i.password:
            request.session['name']=i.first_name+" "+i.last_name
            request.session['name1']=username
            request.session['email']=i.email_id
            return HttpResponseRedirect('/home/')
    else:
        return render(request,'invalid.html')


def registration(request):
    firstname = request.POST.get('fname')
    lastname = request.POST.get('lname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    request.session['email']=email
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    for i in register.objects.all():
        if username == i.username:
            return render(request, 'pass.html', {'error': 'This username is already taken!!'})
    if pass1 == pass2:
        s=register(first_name=firstname ,last_name=lastname,username=username,email_id=email,password=pass1)
        s.save()
        request.session['name'] = firstname + " " + lastname
        request.session['name1'] = username
        return HttpResponseRedirect('/home/')
    else:
        return render(request,'pass.html',{'error':'Re Enter same password!!'})


def logout(request):
    del request.session['name']
    del request.session['name1']
    return HttpResponseRedirect('/home/')


def forgotpassword(request):
    c = {}
    c = c.update(csrf(request))
    return render(request, 'forgotpassword.html', c)


def newpassword(request):
    c = {}
    c = c.update(csrf(request))
    email = request.POST.get('email')
    request.session['name2'] = email
    for i in register.objects.all():
        if email==i.email_id:
            return render(request, 'newpassword.html', c)
    else:
        return render(request, 'forgotpassword.html', {'msg1': 'Your Email is not registered'})


def addnewpassword(request):
    password = request.POST.get('pass', '')
    cpass = request.POST.get('cpass', '')
    if password != cpass:
        return render(request, 'newpassword.html', {'msg1': 'Can not change password. Your both Passwords are different'})
    else:
        target = register.objects.get(email_id=request.session['name2'])
        target.password = password
        target.save()
        del request.session['name2']
        return render(request, 'login.html', {'msg1': 'Password successfully changed.'})


def profile(request):
    c = {}
    for i in register.objects.all():
        if i.username == request.session['name1']:
            c = {
                'username': i.username,
                'password': i.password,
                'fName': i.first_name,
                'lName': i.last_name,
                'email': i.email_id,
            }
    return render(request, 'profile.html', c)


def editprofile(request):
    c = {}
    for i in register.objects.all():
        if i.username == request.session['name1']:
            c = {
            'username': i.username,
            'password': i.password,
            'fName': i.first_name,
            'lName': i.last_name,
            'email': i.email_id,
        }
    return render(request, 'editprofile.html', c)


def profileverification(request):
    firstname = request.POST.get('fName')
    lastname = request.POST.get('lName')
    username = request.POST.get('username')
    email = request.POST.get('email')
    pass1 = request.POST.get('password')
    pass2 = request.POST.get('cpassword')
    if pass1 != pass2:
        for i in register.objects.all():
            if i.username == request.session['name1']:
                c = {
                    'msg':'Both password must be same',
                    'username': i.username,
                    'password': i.password,
                    'fName': i.first_name,
                    'lName': i.last_name,
                    'email': i.email_id,
                }
            return render(request, 'editprofile.html', c)
    else:
        for i in register.objects.all():
            if i.username == request.session['name1']:
                    u1=i.username
                    p1=i.password
                    f1=i.first_name
                    l1=i.last_name
                    e1=i.email_id

        register.objects.filter(username=request.session['name1']).delete()
        for i in register.objects.all():
            if username== i.username:
                c = {
                    'msg':'Username is Already Taken' ,
                    'username':u1,
                    'password':p1,
                    'fName': f1,
                    'lName': l1,
                    'email': e1,
                }
                return render(request, 'editprofile.html', c)
        q = register(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email_id=email,
            password=pass1
        )
        q.save()
        request.session['name'] = firstname + " " + lastname
        request.session['name1'] = username
        c = {}
        for i in register.objects.all():
            if i.username == request.session['name1']:
                c = {
                    'msg1': 'Data Updated',
                    'username': i.username,
                    'password': i.password,
                    'fName': i.first_name,
                    'lName': i.last_name,
                    'email': i.email_id,
                }
        return render(request, 'profile.html', c)



