from django.shortcuts import render
from post.models import Post

def home(request):
    posts = Post.objects.all().order_by("-publishing_date")
    return render(request, "posts/index.html", {"posts": posts})

   