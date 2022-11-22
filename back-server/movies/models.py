from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

# https://image.tmdb.org/t/p/w500/c6OLXfKAk5BKeR6broC8pYiCquX.jpg

POSTER_BASIC_URL = "https://image.tmdb.org/t/p/w500/"

# 장르 속성 먼저 던져놓기 (무비의 다대다 필드로 쓸 예정)
class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


# 영화 모델
class Movie(models.Model):
    tmdb_id = models.CharField(max_length=20)
    # kmdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    overview = models.TextField(blank=True)
    popularity = models.FloatField(null=True)
    vote_average = models.FloatField(null=True)
    adult = models.BooleanField(default=False)
    # 포스터 디폴트 값은 임시로 그 여자 작사 그 남자 작곡 
    poster_path = models.TextField(default="https://image.tmdb.org/t/p/w500/d9C2H1qoFt9AL4DwRlqEEZK4hVa.jpg")
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_like_movies")


# 이 부분 혹시 리뷰 -> 댓글 형식으로 추가하고 싶으시면 말씀 주세욥. 그 부분 소스로 따로 짜놨습니다.
# 댓글 모델 (유저, 영화를 외래키로 쓰고 / 제목, 내용을 받아서 )
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comment_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_like_comment")
    # def __str__(self):
    #     return self.user_id

