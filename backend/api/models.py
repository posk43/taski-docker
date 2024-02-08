"""Это документация для вашего модуля."""
from django.db import models


class Task(models.Model):
    """
    Docstring for YourModel class.

    This class represents...

    Additional details about the class and its functionality.
    """

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
