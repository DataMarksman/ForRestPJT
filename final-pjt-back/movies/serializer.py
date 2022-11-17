from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

# 영화 리스트를 보여주는 시리얼라이저
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('movie_id', 'title','poster_path')

# 영화 검색 리스트를 보여주는 시리얼라이저
class MovieSearchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('movie_id', 'title','poster_path','rating','release_date', 'popularity')


# 개봉 중인 영화리스트를 보여주는 시리얼라이저
class BoxMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoxMovie
        fields = ('movie_id', 'title','poster_path','rating','release_date', 'popularity')

# 댓글 리스트를 보여주는 시리얼라이저
class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('movie_id', 'content')


# 영화 상세페이지 시리얼라이저
class MovieDetailSerializer(serializers.ModelSerializer):
    # class GenreSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Genre
    #         fields = ('genre',)

    # genre = GenreSerializer(many=True, read_only=True)
    # review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('movie_id', 'title','overview','poster_path','rating','release_date', 'popularity')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('movie_id', 'content','created_at','updated_at')

