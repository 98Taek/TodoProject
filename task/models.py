from django.db import models


class TodoBase(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Task(models.Model):
    level = ((0, '1'), (1, '2'), (2, '3'), (3, '4'), (4, '5'))
    title = models.CharField(max_length=100)
    description = models.TextField()
    todolist = models.ForeignKey(TodoBase, on_delete=models.CASCADE, related_name='tasks')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    important = models.IntegerField(choices=level)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
