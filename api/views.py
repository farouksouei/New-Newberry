from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from api.models import Article

# Create your views here.


def article_list(request):

    # get all articles
    if request.method == 'GET':
        article = Article.objects.all()
