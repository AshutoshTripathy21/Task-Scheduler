# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .utils import efficient_sort
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string

def home(request):
    pending_tasks = Task.objects.filter(completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    
    # Sort tasks efficiently based on priority
    pending_tasks = efficient_sort(pending_tasks)
    completed_tasks = efficient_sort(completed_tasks)
    
    context = {'pending_tasks': pending_tasks, 'completed_tasks': completed_tasks}
    return render(request, 'task_list.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            user_email = form.cleaned_data.get('email')
            send_email_notification(user_email, task)
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})

def send_email_notification(email, task):
    subject = 'Task Reminder: Deadline approaching'
    message = render_to_string('email_notification_template.html', {'task': task})
    sender_email = 'exampleflask365@outlook.com'
    recipient_list = [email]

    send_mail(subject, message, sender_email, recipient_list)

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'update_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.completed_at = timezone.now()
    task.save()
    return redirect('home')


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {'task': task}
    return render(request, 'task_detail.html', context)