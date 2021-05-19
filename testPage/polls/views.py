from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse

# Create your views here.
def indexfunc(request):
    if request.user.is_authenticated:
        return redirect('userpage')
    else:
        return render(request, 'index.html', {'message': 'Hello, World!!!'})
    
def signupfunc(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': "既登録済"})
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userpage')
        else:
            return render(request, 'login.html', {'context': 'not logged in'})
    return render(request, 'login.html', {'context': 'get method'})

@login_required
def userpagefunc(request):
    username = 'Hello, ' + request.user.get_username() + '!!!'
    return render(request, 'userpage.html', {'message': username})

def logoutfunc(request):
    logout(request)
    return redirect('index')