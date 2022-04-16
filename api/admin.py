from datetime import date
from django.contrib import admin
from .models import Article

# Register your models here

# admin.site.register(Article)


@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description', 'created_at')
    list_display = ('title', 'description')
    date_hierarchy = ('created_at')
