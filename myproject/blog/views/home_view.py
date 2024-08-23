from django.shortcuts import render

# Create your views here.

def renderHomepage(request):
    return render(request,'home/index.html')


def renderCreateBlogPage(request):
    return render(request,'home/create_blog.html')