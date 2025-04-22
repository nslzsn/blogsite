
from django.contrib import admin
from django.urls import path, include
from home.views import home
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("post/", include("post.urls")),
    path("accounts/", include("accounts.urls")),
    path('tasks/', include('task.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = 'home.views.custom_bad_request_view'
handler403 = 'home.views.custom_permission_denied_view'
handler404 = 'home.views.custom_page_not_found_view'
handler500 = 'home.views.custom_error_view'
