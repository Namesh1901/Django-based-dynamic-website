from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/travello')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/accounts/login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('/accounts/register')
            else:
                user=User.objects.create_user(username=username,last_name=lastname,first_name=firstname,email=email,password=pass1)
                user.save()
                return redirect('/accounts/login')
        else:
            messages.info(request,'Password Not Matching')
            return redirect('/accounts/register')
        return redirect('/travello')
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/travello')
    