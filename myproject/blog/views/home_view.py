from django.shortcuts import render, redirect, get_object_or_404
from ..models import Blog

# Create your views here.



# Create a new blog post
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        blog = Blog(title=title, subtitle=subtitle, description=description, image=image)
        blog.save()

        return redirect('blog_list')  # Redirect to the list of blog posts

    return render(request, 'home/create_blog.html')

# List all blog posts
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'home/blog_list.html', {'blogs': blogs})

# View a single blog post
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'home/blog_detail.html', {'blog': blog})

# Update an existing blog post
def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.subtitle = request.POST.get('subtitle')
        blog.description = request.POST.get('description')
        if request.FILES.get('image'):
            blog.image = request.FILES.get('image')
        blog.save()

        return redirect('blog_detail', blog_id=blog.id)

    return render(request, 'home/update_blog.html', {'blog': blog})

# Delete a blog post
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')

    return render(request, 'home/delete_blog.html', {'blog': blog})