from django import forms

from task.models import TodoBase, Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoBase
        fields = ['title']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important', 'completed']
