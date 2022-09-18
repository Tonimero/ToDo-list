from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
    
#     class Profile(models.Model):
#     first_name = models.CharField(max_length=500)
#     last_name = models.CharField(max_length=500)
#     email = models.EmailField(max_length=300, unique=True)
#     password = models.CharField(max_length=500)
#     profile_pic = models.ImageField(upload_to="static/images/profile_picture/", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Category(models.Model):
#     pass

# class PostModel(models.Model):
#     title = models.CharField( max_length=5000)
#     slug = models.SlugField()
#     description = models.TextField()
#     image = models.ImageField( upload_to="static/images/blog_post_image/", blank=False)
#     status_type = (
#         ('Pub', 'Published'),
#         ('UnPub', 'Unpublished'),
#     )
#     status = models.CharField(choices=status_type, max_length= 12)
    
#     def __str__(self):
#         return self.title
