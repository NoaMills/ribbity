from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from django.views.generic import ListView
from tasks.models import Task
from django.views.generic.detail import DetailView
from .forms import TaskForm
from .models import Task

def todays_day_of_the_week():
    today = date.today().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week_name = days[today]
    return day_of_week_name



def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def home(request):
    context = {"day": todays_day_of_the_week()}
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    tasks = Task.objects.all()
    context['tasks'] = tasks
    return render(request, 'home.html', context)

class TaskListView(ListView):
    model = Task
    context_object_name='tasks'

class TaskDetailView(DetailView):
    model = Task

# def new_task(request):
#     context = {}
#     form = TaskForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context['form'] = form
#     return render(request, 'home.html', context)

def mark_as_completed(request, id):
    task = get_object_or_404()
    pass
