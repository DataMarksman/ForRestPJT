from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    user_profile_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

