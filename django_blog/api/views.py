from django.shortcuts import render
from rest_framework import viewsets, pagination
from .serializers import ProfileSerializer, UserSerializer, ArticleSerializer
from member.models import Profile
from article.models import Article
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer