from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model): 
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs',default=1)

    def __str__(self):
        return self.title