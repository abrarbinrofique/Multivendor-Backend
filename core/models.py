from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .constants import USER_TYPES

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=USER_TYPES, default="none")
    shipping_address = models.CharField(max_length=500, default="Not Set")

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def post_user_save(sender, instance, **kwargs):
    try:
        profile = UserProfile(user=instance)
        profile.save()
    except:
        pass