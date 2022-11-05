from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    """
        This is creating a table in the database with the following columns:
        user, title, description, task_complete, create_date.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    task_complete = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returning the title of the task.
        """
        return self.title

    class Meta:
        """Ordering the tasks by whether they are complete or not."""
        ordering = ['task_complete']
