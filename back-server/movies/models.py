from django.db import models
from django.conf import settings

# Create your models here.
# class Article(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# 영화 모델
class Movie(models.Model):
    tmdb_id = models.CharField(max_length=20)
    # kmdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    overview = models.TextField(blank=True)
    release_date = models.CharField(max_length=50)
    popularity = models.IntegerField(null=True)
    # 포스터 잠시 보류
    # poster_path = models.URLField(_(""), max_length=200, blank=True)

# 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

