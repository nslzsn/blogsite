
from django.contrib import admin
from django.urls import path, include
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("post/", include("post.urls")),
    path("accounts/", include("accounts.urls")),
]
