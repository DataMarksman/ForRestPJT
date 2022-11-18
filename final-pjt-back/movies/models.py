from django.db import models
from django.contrib.postgres.fields import ArrayField  
from django.conf import settings
# Create your models here.

# 세부 내역은 일단 보류하고, 밑에 All_in_one으로 일단 진행해볼 예정
# ## Movie 모델

# class Movie(models.Model):
#     title = models.CharField(max_length=50)
#     release_date = models.DateField(auto_now=False, auto_now_add=False)
#     poster_url = models.URLField(max_length=400)
#     overview = models.TextField()

# # 장르 모델

# class Genre(models.Model):
#     genre_name = models.TextField()

# class MovieGenre(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)


# # 플랫폼 모델

# class PlatForm(models.Model):
#     platform_name = models.CharField(max_length=20)
#     platform_img =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

# class Movie_PlatForm(models.Model):
#     platform_id = models.ForeignKey(PlatForm, on_delete=models.CASCADE)
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    





"""
임시 픽스    
"""

# # All_in_one Movie 모델

# class Movie(models.Model):
#     movie_id = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     overview = models.TextField()
#     # 포스터 사진은 뒤의 URL 추가 주소만 받고 앞의 URL 기본값을 넣고 돌리자.
#     poster_path = models.TextField()
#     director = models.CharField(max_length=30)
#     director_poster = models.TextField(null=True)
#     # actors = models.ManyToManyField(Actor,related_name='movies')
#     # rating = models.FloatField(max_length=10,null=True)
#     release_date = models.DateTimeField(null = True)
#     popularity = models.IntegerField()
#     # genre = models.ManyToManyField(Genre, related_name='movies')
#     genre = ArrayField(models.CharField(max_length=10), blank=True)  


# # 현재 개봉 중인 영화
# class BoxMovie(models.Model):
#     box_id = models.CharField(max_length=100)
#     box_rank = models.IntegerField()
#     box_title = models.CharField(max_length=100)
#     box_en_title = models.CharField(max_length=100)
#     # 이 부분은 나중에 TMDB랑 연동 예정
#     box_poster_path = models.TextField(blank=True)


# # 댓글 모델
# class Comment(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# # class Rating(models.Model):
# #     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
# #     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Movie(models.Model):
    tmdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    overview = models.TextField()
    release_date = models.DateTimeField(null = True)
    popularity = models.IntegerField()
    genre = ArrayField(models.CharField(max_length=10), blank=True)  

