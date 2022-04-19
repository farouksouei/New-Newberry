
from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
#from .views import article_list, article_detail
urlpatterns = [

    path('', include(router.urls)),


    #path('articles', ArticleList.as_view()),
    #path('articles/<int:pk>', ArticleDetail.as_view()),

    #path('articles', article_list),
    #path('articles/<int:pk>', article_detail),

]
