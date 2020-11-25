from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',articleViewSet,basename='article')

urlpatterns = [

    path('viewset/',include(router.urls)),

    path('article/',article_list),
    path('detail/<int:pk>/',article_detail),

    #Class API View
    path('articleClassApi/',articleApiView.as_view()),
    path('detailApi/<int:pk>/',article_detail_api.as_view()),

    #Generic Based views
    path('generic/article/<int:id>/',genericAPiView.as_view()),
]