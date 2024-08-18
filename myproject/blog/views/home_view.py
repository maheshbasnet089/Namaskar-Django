from django.shortcuts import render

# Create your views here.

def renderHomepage(request):
    return render(request,'home/index.html')