from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE, DO_NOTHING
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

# Create your models here.


class DIFFICULTLY_CHOICES(models.IntegerChoices):
    EASY = 0, "Easy"
    MEDIUM = 1, "Medium"
    HARD = 2, "Hard"


class TASK_STATUS_CHOICES(models.IntegerChoices):
    IN_DEVELOPMENT = 0, "In-Development"
    ACCEPTED = 1, "Accepted"


class TASK_LANGUAGE_CHOICES(models.IntegerChoices):
    PYTHON = 0, "Python"
    SQL = 1, "SQL"


class Tasks(BaseModel):
    name = models.CharField(
        max_length=280, unique=True, help_text=_("Name must be unique and max length is 280 characters.")
    )
    difficulty = models.PositiveSmallIntegerField(
        choices=DIFFICULTLY_CHOICES.choices, default=DIFFICULTLY_CHOICES.MEDIUM
    )
    category = models.CharField(
        max_length=24, choices=[("Math", "Math"), ("DB", "DataBase"), ("Algorithms", "Algorithms")]
    )
    description = models.TextField(max_length=2400)
    constraints = models.CharField(max_length=240)
    tests = models.ForeignKey("problems.Tests", on_delete=DO_NOTHING)
    edited = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="tasks/images", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.difficulty} {self.category} {self.created_at}"


class Tests(BaseModel):
    count_tests = models.IntegerField()
    tests = models.FilePathField(path="src/problems/tasks/tests_for_tasks")

    def __str__(self):
        return f"{self.tests} {self.count_tests}"


class Solutions(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    task = models.ForeignKey(Tasks, on_delete=DO_NOTHING)
    language = models.PositiveSmallIntegerField(choices=TASK_LANGUAGE_CHOICES.choices)
    solution = models.TextField(max_length=4200)
    status = models.PositiveSmallIntegerField(
        choices=TASK_STATUS_CHOICES.choices, default=TASK_STATUS_CHOICES.IN_DEVELOPMENT
    )
    time = models.PositiveIntegerField()
    memory = models.FloatField()
    test_passed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} {self.task.name} {self.language} status: {self.status} memory: {self.memory}mb time: {self.time}ms test_passed: {self.test_passed}"
