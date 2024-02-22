from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .utils import efficient_sort

def home(request):
    tasks = Task.objects.all()
    sorted_tasks = efficient_sort(tasks)
    context = {'tasks': sorted_tasks}
    return render(request, 'task_list.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})
