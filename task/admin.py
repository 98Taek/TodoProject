from django.contrib import admin

from task.models import TodoBase, Task


@admin.register(TodoBase)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated', 'important', 'completed']
    raw_id_fields = ['todolist']
    list_filter = ['created', 'important', 'completed']
