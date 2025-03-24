from django.contrib import admin
from django.urls import path
from home.views import home
from post.views import post_index, post_create, post_detail, post_update, post_delete
from django.utils.text import slugify

app_name = 'post'

urlpatterns = [
    path('index/', post_index, name='index'),
    path('create/', post_create, name='creat'),
    path('<slug:slug>/', post_detail, name='detail'),
    path('<slug:slug>/update/', post_update, name='update'),
    path('<slug:slug>/delete/', post_delete, name='delete'),
]