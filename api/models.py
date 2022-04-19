import imp
from pydoc import describe
from venv import create
from django.db import models
from datetime import datetime


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
