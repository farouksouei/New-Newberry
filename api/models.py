import imp
from pydoc import describe
from venv import create
from django.db import models
from datetime import datetime

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
#from api.models import Article
#from api.serializers import ArticleSerializer
