# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    email = forms.EmailField(label='Your Email', required=True)
    class Meta:
        model = Task
        fields = ['title', 'priority', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }