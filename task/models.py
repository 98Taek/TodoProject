from django.contrib.auth.models import User
from django.db import models


class TodoBase(models.Model):
    creator = models.ForeignKey(User, related_name='todo_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Task(models.Model):
    class ChoiceLevel(models.TextChoices):
        LOW = 'Low'
        NORMAL = 'Normal'
        HIGH = 'High'

    creator = models.ForeignKey(User, related_name='task_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    todolist = models.ForeignKey(TodoBase, on_delete=models.CASCADE, related_name='tasks')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    important = models.CharField(max_length=6, choices=ChoiceLevel.choices, default=ChoiceLevel.NORMAL)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
