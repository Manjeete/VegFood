from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        name = request.POST['register_name']
        username = request.POST['register_username']
        email = request.POST['register_email']
        password = request.POST['register_password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is Taken')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This Email is already in used !')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
                user.save()
                return redirect('index')
    else:
        return render(request, 'accounts/login.html') 

def login(request):
    if request.method=='POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('login')                
    else:
        return render(request, 'accounts/login.html')    

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are now logged Out")
        return render(request,'accounts/login.html')