from django.contrib import admin

from task.models import TodoBase, Task


@admin.register(TodoBase)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated', 'important', 'completed']
    raw_id_fields = ['todolist']
