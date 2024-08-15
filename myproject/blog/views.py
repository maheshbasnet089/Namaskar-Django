from django.shortcuts import render

# Create your views here.

def renderRegisterForm(request):
    return render(request,'auth/register.html')

def renderLoginForm(request):
    return render(request,'auth/login.html')