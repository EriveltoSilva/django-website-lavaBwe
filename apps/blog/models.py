from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField()
    summary = RichTextField(default='')
    image_thumb = models.ImageField(upload_to="blog/Post/", blank=True)
    image_alt = models.CharField(max_length=75, default="",blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    # def get_absolute_url(self):
        # return reverse('filter', args=[str(self.id)])
    
    def get_absolute_url(self):
        return reverse('blog')

class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField()
    summary = RichTextField(default='')
    content = RichTextUploadingField()
    image_thumb = models.ImageField(upload_to="app_blog/posts/", blank=True)
    image_alt = models.CharField(max_length=75, default="",blank=True)
    category = models.ForeignKey(to=Category, on_delete = models.PROTECT, null=False, related_name='Post')
    author = models.ForeignKey(to=User, on_delete = models.PROTECT, null=True, related_name='post_author')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('blog-article', args=[str(self.id)])
    
class Comment(models.Model):
    content = models.TextField(max_length=255, null=False, blank=False)
    slug = models.SlugField()
    author = models.ForeignKey(to=User, on_delete = models.CASCADE, null=False, related_name='comment_author')
    published = models.BooleanField(default=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.author.get_full_name()}'s comment."



class NewletterAssinature(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name}-{self.email}"
