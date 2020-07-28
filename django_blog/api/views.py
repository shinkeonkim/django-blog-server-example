from django.shortcuts import render
from rest_framework import viewsets, pagination
from .serializers import ProfileSerializer, UserSerializer, ArticleSerializer
from member.models import Profile
from article.models import Article
from django.contrib.auth.models import User

from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer


# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def articles_function(request):
    articles = Article.objects.filter(updated_at__isnull=False).order_by('updated_at')
    article_list = serializers.serialize('json', articles)
    return HttpResponse(article_list, content_type="text/json-comment-filtered")