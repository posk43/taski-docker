"""Это документация для вашего модуля."""
from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
    """
    This class represents...

    Additional details about the class and its functionality.
    """

    def setUp(self):
        """Set up test client."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Test the availability of the task list."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Test task creation."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
