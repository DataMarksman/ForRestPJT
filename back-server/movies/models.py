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

# https://image.tmdb.org/t/p/w500/c6OLXfKAk5BKeR6broC8pYiCquX.jpg

POSTER_BASIC_URL = "https://image.tmdb.org/t/p/w500/"

# 영화 모델
class Movie(models.Model):
    tmdb_id = models.CharField(max_length=20)
    # kmdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    overview = models.TextField(blank=True)
    popularity = models.FloatField(null=True)
    # 포스터 디폴트 값은 임시로 그 여자 작사 그 남자 작곡 
    poster_path = models.TextField(default="https://image.tmdb.org/t/p/w500/d9C2H1qoFt9AL4DwRlqEEZK4hVa.jpg")
    


# 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Movie_Info(models.Model):
#     tmdb_id = models.CharField(max_length=20)
#     title = models.CharField(max_length=50)
#     overview = models.TextField(blank=True)
#     release_date = models.CharField(max_length=50)
#     popularity = models.IntegerField(null=True)
#     poster_path = models.TextField(default="d9C2H1qoFt9AL4DwRlqEEZK4hVa.jpg")