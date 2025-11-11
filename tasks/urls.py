from django.urls import path
from tasks.views import TaskListView, TaskDetailView

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    # path("tasks/", TaskListView.as_view(), name='task-list'),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name='task-detail'),
    # path("tasks/new-task/", views.new_task, name="new-task")
]