from django import forms
from .models import *


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'date', 'done']
