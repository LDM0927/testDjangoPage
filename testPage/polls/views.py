from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error': "既登録済"})
    
    return render(request, 'signup.html')

