from django.urls import path
from tasks.views import TaskListView, TaskDetailView

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("tasks/", TaskListView.as_view()),
    path("tasks/<int:pk>/", TaskDetailView.as_view()),
    path("tasks/new-task/", views.new_task, name="new-task")
]