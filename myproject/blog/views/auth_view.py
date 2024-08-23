
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

def renderRegisterForm(request):
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      print(username,password,email)
      user = User.objects.create(
        username = username, 
        email = email, 
      )
      user.set_password(password)
      user.save()
      print(user, "User")
      return redirect('/blog/login')

    else:
        return render(request,'auth/register.html')


def renderLoginForm(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None: 
            login(request,user)
            return redirect('/')
        else: 
            messages.error(request,"Invalid email or password")
            return redirect('/blog/login')
    return render(request,'auth/login.html')