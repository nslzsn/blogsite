

from django.contrib import admin
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_assigned_to', 'status',  'created_at', 'due_date', 'attachment')
    list_editable = ('status', 'due_date')  
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'assigned_to__username')
    autocomplete_fields = ['assigned_to']
    filter_horizontal = ('assigned_to',)

    def get_assigned_to(self, obj):
        return ", ".join([user.username for user in obj.assigned_to.all()])
    get_assigned_to.short_description = 'Atanan Kişiler'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
