from django.db import models

# Create your models here.


## Movie 모델

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    poster_url = models.URLField(max_length=400)
    overview = models.TextField()

# 장르 모델

class Genre(models.Model):
    genre_name = models.TextField()

class MovieGenre(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)


# 플랫폼 모델

class PlatForm(models.Model):
    platform_name = models.CharField(max_length=20)
    platform_img =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

class Movie_PlatForm(models.Model):
    platform_id = models.ForeignKey(PlatForm, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    



# 댓글 모델
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# 