from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.upload_article, name = "upload_article" ),
    path('show/', views.show_articles, name = "show_articles" )

]