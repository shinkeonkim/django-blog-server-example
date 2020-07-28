from django.conf.urls import  url, include
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'profile', views.UserViewSet)
# router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    path("articles/", views.articles_function, name = "articles"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]