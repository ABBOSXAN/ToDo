from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import TaskCreateForm
from .models import Task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_edit.html'
    fields = ['title', "descript", "deadline"]

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url=reverse_lazy('index')

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = TaskCreateForm
    success_url = reverse_lazy('index')
