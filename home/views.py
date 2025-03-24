from django.shortcuts import render
from post.models import Post

def home(request):
    posts = Post.objects.all().order_by("-publishing_date")
    return render(request, "posts/index.html", {"posts": posts})

def custom_error_view(request, exception=None):
    return render(request, 'error.html', status=500)

def custom_permission_denied_view(request, exception=None):
    return render(request, 'error.html', status=403)

def custom_page_not_found_view(request, exception=None):
    return render(request, 'error.html', status=404)

def custom_bad_request_view(request, exception=None):
    return render(request, 'error.html', status=400)
