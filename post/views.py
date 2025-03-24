from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.

def home(request):
    return HttpResponse("<b> hosgeldiniz </b>") 

def post_index(request):
    posts=Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


@login_required(login_url='/accounts/login/')
def post_create(request):
    if not request.user.is_authenticated:
        raise Http404("giriş yapmalısınız")
    
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)  
            post.slug = slugify(post.title)
            post.author = request.user 
            post = form.save()
            messages.success(request, "Başarılı bir şekilde oluşturuldu")
            return HttpResponseRedirect(post.get_absolute_url())
            
        else:
            print(form.errors)
    
    context = {
        "form": form
    }
   
    return render(request, 'posts/form.html', {'form': form})
    


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post,
    }

    return render(request, "posts/detail.html", {"post": post})




def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # 👇 Yetki kontrolü
    if post.author != request.user:
        raise Http404("Bu gönderiyi düzenleme yetkiniz yok.")

    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = request.user
            updated_post.save()
            messages.success(request, "Gönderi güncellendi.")
            return HttpResponseRedirect(updated_post.get_absolute_url())
        else:
            print(form.errors)

    return render(request, "posts/form.html", {"form": form})



def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        raise Http404("Bu gönderiyi silme yetkiniz yok.")
    if request.method == "POST":
        post.delete()
        messages.success(request, "Gönderi silindi.")
        return redirect("posts:index")  # ya da kendi ana sayfan

    return render(request, "posts/confirm_delete.html", {"post": post})