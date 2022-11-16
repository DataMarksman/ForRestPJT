from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    # 유저 프로필 사진. default 값을 뭘로줄지 애매함...
    # user_profile_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    user_profile_img = models.ImageField(upload_to='images/user_photos', null=True)
    
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers')
    
    # 유저의 플랫폼 구독 기능을 추가하려면? 임시 파트
    # platform_subscribe = models.JSONField(default=dict, null=True)
    
    """
    생략된 필드
    id
    username
    first_name
    last_name
    email
    password
    is_staff
    is_activate
    is_superuser
    last_login
    date_joined
    """
