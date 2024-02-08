"""Это документация для вашего модуля."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Docstring for YourModel class.

    This class represents...

    Additional details about the class and its functionality.
    """

    class Meta:
        """Это документация для вашего класса."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
