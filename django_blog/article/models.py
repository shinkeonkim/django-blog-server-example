from django.db import models

from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.utils import timezone
from mdeditor.fields import MDTextField

def date_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return os.sep.join([ymd_path, uuid_name + extension])

class Article(models.Model):
    title = models.CharField(max_length = 200)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    body = MDTextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    article = models.ForeignKey(Article, default = None,  on_delete = models.CASCADE)
    image = models.ImageField(upload_to = date_upload_to, verbose_name = 'Image')