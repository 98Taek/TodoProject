from django.shortcuts import render, redirect

from task.forms import TodoForm
from task.models import TodoBase, Task


def todo_list(request):
    todos = TodoBase.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    return render(request, 'task/list.html', {'todos': todos, 'form': form})


def task_list(request, todo_id):
    tasks = Task.objects.filter(id=todo_id)
    return render(request, 'task/task_list.html', {'tasks': tasks})


def task_update(request):
    pass


def task_delete(request):
    pass
