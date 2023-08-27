from django.shortcuts import render, redirect, get_object_or_404

from task.forms import TodoForm, TaskForm
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
    todo = get_object_or_404(TodoBase, id=todo_id)
    tasks = todo.tasks.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.todolist = todo
            form.save()
    else:
        form = TaskForm()
    return render(request, 'task/task_list.html', {'tasks': tasks, 'form': form})


def todo_delete(request, todo_id):
    todo = TodoBase.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('task:home')
    return render(request, 'task/delete.html', {'todo': todo})
