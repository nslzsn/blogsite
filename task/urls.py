from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "task"

urlpatterns = [
    path('go/', views.task_redirect_view, name='task_redirect'),
    path('my-tasks/', views.user_task_list, name='user_task_list'),
    path('admin-panel/', views.admin_task_panel, name='admin_task_panel'),
    path('update-status/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)