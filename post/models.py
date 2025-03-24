from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name="başlık")
    content  = models.TextField(verbose_name="içerik")
    slug = models.SlugField(unique=True, blank=True, null=True)
    publishing_date= models.DateTimeField(verbose_name="yayımlanma tarihi", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.slug})
