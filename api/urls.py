from django.urls import path
from .views import ArticleList, ArticleDetail
#from .views import article_list, article_detail
urlpatterns = [
    path('articles', ArticleList.as_view()),
    path('articles/<int:pk>', ArticleDetail.as_view()),

    #path('articles', article_list),
    #path('articles/<int:pk>', article_detail),

]
