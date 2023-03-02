from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .forms import *
from .models import *


class TasksList(ListView):
    model = Task
    template_name = 'todo/taskslist.html'
    context_object_name = 'tasks'


class AddTask(CreateView):
    form_class = AddTaskForm
    # model = Task
    # fields = ['title', 'description', 'date', 'done']
    template_name = 'todo/addtask.html'
