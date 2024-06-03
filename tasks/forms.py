from django.db import models
from django.forms import ModelForm
from .models import Task

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descript', 'author', 'task_created_date', 'deadline']
        author=models.ForeignKey(
            'auth.User', on_delete=models.CASCADE
        )