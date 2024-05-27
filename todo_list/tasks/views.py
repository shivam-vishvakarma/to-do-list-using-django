from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        Task.objects.create(task_name=task_name)
    return redirect('task_list')

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('task_list')
