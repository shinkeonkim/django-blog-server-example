from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(blank = True, null = True)
    location = models.CharField(blank = True, null = True, max_length = 40)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    
@receiver(post_save, sender = User)
def save_user_profilepost_save(sender, instance, **kwargs):
    instance.profile.save()




