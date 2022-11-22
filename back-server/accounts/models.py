from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre, Comment


# 유저 모델 제작 (기본은 깔고 들어가고, 팔로잉 기능과 프로필 이미지, 선호 장르를 넣었다.)
class User(AbstractUser):
    followings = models.ManyToManyField("self", symmetrical=False, related_name = 'followers')
    profile_img = models.ImageField(blank=True, upload_to='images/', null=True)
    genre_like = models.ManyToManyField(Genre, related_name="user_genre")
    
    # def __str__(self):
    #     return self.pk
    # 일단 comment like는 comment에 묶여있음
    # comment_like = models.ManyToManyField(Comment, related_name="user_comment")
    
    # platform_subscribe = models.ManyToManyField()

