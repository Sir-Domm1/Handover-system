from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('Login')

    return render(request, 'Login.html')

def Logout(request):
    auth.logout(request)
    messages.success(request,'Successfully Logged out')
    return redirect('Login')
    
def Signup(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Password==Confirm_Password:
            if User.objects.filter(email=Email).exists():
                messages.info(request, 'Email already used, try another one')
                return redirect('signup')

            elif User.objects.filter(username=Username).exists():
                messages.info(request, 'Username already used, try another one')
                return redirect('signup')
            
            else:
                user=User.objects.create_user(username=Username,email=Email,password=Password)
                user.save()
                return redirect('Login')
        else:
            message.info(request,'The passwords do not match, input correct passwords')
            return redirect('signup')

    return render(request, 'signup.html')

    