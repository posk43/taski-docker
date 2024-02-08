"""Это документация для вашего класса."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Это документация для вашего класса."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
