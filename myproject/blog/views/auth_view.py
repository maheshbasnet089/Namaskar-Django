from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.

def renderRegisterForm(request):
      if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        username = request.POST["username"]
        user =  User.objects.create(
            username = username,
            email = email, 
        )
        user.set_password(password)
        user.save()
        return redirect('/blog/login') 
      else:  
        return render(request,'auth/register.html')

def renderLoginForm(request):
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request,username=username,password=password)
      print(user)
      if user is not None:
        login(request,user)
        return redirect('/') 
      else:
         messages.error(request,"Invalid username or password")
         return redirect("/blog/login")
    else:
      return render(request,'auth/login.html')

def renderHomepage(request):
    return render(request,'home/index.html')


