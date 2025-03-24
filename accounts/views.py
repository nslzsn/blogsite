from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Kayıt başarılı! Giriş yapabilirsiniz.")
            return redirect("accounts:login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get("next") or "post:index"
            return redirect(next_url)
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")
