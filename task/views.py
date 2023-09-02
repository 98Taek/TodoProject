from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from task.forms import TodoForm, TaskForm
from task.models import TodoBase, Task


@login_required
def todo_list(request):
    todos = TodoBase.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.creator = request.user
            form.save()
            return redirect('task:home')
    else:
        form = TodoForm()
    return render(request, 'task/list.html', {'todos': todos, 'form': form})


@login_required
def task_list(request, todo_id):
    todo = get_object_or_404(TodoBase, id=todo_id)
    tasks = todo.tasks.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.todolist = todo
            form.creator = request.user
            form.save()
            return redirect('task:task_list', todo_id)
    else:
        form = TaskForm()
    return render(request, 'task/task_list.html', {'todo': todo, 'tasks': tasks, 'form': form})


def todo_delete(request, todo_id):
    todo = TodoBase.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('task:home')
    return render(request, 'task/delete.html', {'todo': todo})


def task_delete(request, todo_id, task_id):
    todo = TodoBase.objects.get(id=todo_id)
    task = Task.objects.get(id=task_id, todolist=todo)
    task.delete()
    return redirect('task:task_list', todo_id)
