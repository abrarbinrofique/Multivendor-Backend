from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .constants import USER_TYPES

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=USER_TYPES, default="none")

@receiver(post_save, sender=User)
def post_user_save(sender, instance, **kwargs):
    profile = UserProfile(user=instance)
    profile.save()