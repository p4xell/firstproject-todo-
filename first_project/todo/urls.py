from django.urls import path
from .views import *

urlpatterns = [
    path('', TasksList.as_view()),
    path('addtask/', AddTask.as_view())
]
