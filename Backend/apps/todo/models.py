from django.db import models

# Create your models here.

class TodoList(models.Model):
    title = models.TextField(max_length=100)

    def __str__(self):
        return self.title