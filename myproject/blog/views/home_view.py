from django.shortcuts import get_object_or_404, render,redirect
from ..models import Blogs

def renderHomepage(request):
    return render(request,'home/index.html')

def home(request):
    blogs = Blogs.objects.all().order_by('-created_at')
    return render(request,"home/blog_list.html",{'blogs' : blogs})

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        blog =  Blogs(title=title,subtitle=subtitle,description=description,image=image)
        blog.save()
        return redirect("home")
    
    return render(request,'home/create_blog.html')

def blog_detail(request,blog_id):
    blog = get_object_or_404(Blogs,pk=blog_id)

    return render(request,"home/blog_detail.html",{'blog':blog})