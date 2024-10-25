from django.contrib import admin

from problems.models import Solutions, Tasks, Tests

# Register your models here.


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin): ...


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin): ...


@admin.register(Solutions)
class SolutionAdmin(admin.ModelAdmin): ...
