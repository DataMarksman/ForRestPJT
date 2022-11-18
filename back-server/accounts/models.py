from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField("self", symmetrical=False, related_name = 'followers')
    user_profile_img = models.ImageField(blank=True, upload_to='images/', null=True)
    platform_subscribe = models.JSONField(default=dict, null=True)

