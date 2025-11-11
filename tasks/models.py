from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

status_choices = {
    "ac": "active",
    "c": "completed",
}

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    status = models.CharField(choices=status_choices, blank=True, null=False, default="ac", max_length=2)
    date_created = models.DateTimeField(auto_now=True, blank=True, null=False)
    date_completed = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    delete_if_deadline_passed = models.BooleanField(blank=True, default=False)
    estimated_duration = models.IntegerField(
        blank=False,
        null=False,
        help_text="An estimate in minutes of the time required to complete this task",
        validators=[
            MinValueValidator(1),
        ]
    )
    description = models.TextField(max_length=1000, blank=True, null=True)
    prerequisites = models.ManyToManyField("self", blank=True, related_name="subsequent_tasks", symmetrical=False)
    priority = models.IntegerField(
        blank=False,
        null=False,
        default=5,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        help_text="The priority of this task on a scale from 1 to 10."
    )
    splittable = models.BooleanField(blank=True, null=False, default=False, help_text="Whether or not this task can be split into separate timeblocks.")
    minimum_split_time = models.IntegerField(blank=True, default=15, help_text="The minimum amount of time to spend on this task in a given timeblock")

    def __str__(self):
        return self.name

def has_cycle(stack, seen):
    if len(stack) == 0:
        return True
    current_id = stack[-1]
    current_task = Task.objects.filter(id=current_id)
    prereqs_id_list = current_task.values_list('prerequisites__id', flat=True)
    for prereq in prereqs_id_list:
        if prereq in stack:
            return True
        if prereq in seen:
            continue
        stack.append(prereq)
        if has_cycle(stack, seen):
            return True
        seen.append(prereq)
        stack = stack[:-1]


