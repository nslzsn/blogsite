

from django.contrib import admin
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_assigned_to', 'status', 'is_completed', 'created_at')
    list_filter = ('status','is_completed', 'created_at', 'tags')
    search_fields = ('title', 'description', 'assigned_to__username')
    autocomplete_fields = ['assigned_to', 'tags']
    filter_horizontal = ('assigned_to','tags',)

    def get_assigned_to(self, obj):
        return ", ".join([user.username for user in obj.assigned_to.all()])
    get_assigned_to.short_description = 'Atanan Kişiler'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
