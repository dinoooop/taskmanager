# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        
        Task.objects.create(title=title, description=description, due_date=due_date, priority=priority)
        return redirect('list_tasks')
    return render(request, 'add_task.html')

def list_tasks(request):
    tasks = Task.objects.all().order_by('due_date')
    priorities = { 1: 'Low', 2: 'Medium', 3: 'High' }
    return render(request, 'list_tasks.html', {'tasks': tasks, 'priorities': priorities})

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.priority = request.POST['priority']
        task.save()
        return redirect('list_tasks')
    return render(request, 'edit_task.html', {'task': task})

# Delete
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('list_tasks')