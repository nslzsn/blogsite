
from django.contrib import admin
from django.urls import path, include
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("post/", include("post.urls")),
    path("accounts/", include("accounts.urls")),
]

handler400 = 'home.views.custom_bad_request_view'
handler403 = 'home.views.custom_permission_denied_view'
handler404 = 'home.views.custom_page_not_found_view'
handler500 = 'home.views.custom_error_view'