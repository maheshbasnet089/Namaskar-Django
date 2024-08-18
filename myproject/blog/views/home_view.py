from django.shortcuts import render

def renderHomepage(request):
    return render(request,'home/index.html')