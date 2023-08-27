from django.urls import path

from task import views

app_name = 'task'

urlpatterns = [
    path('', views.todo_list, name='home'),
    path('task_list/<int:todo_id>/', views.task_list, name='task_list'),
    path('todo_delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
]