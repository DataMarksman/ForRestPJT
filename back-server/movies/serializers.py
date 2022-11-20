from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

POSTER_BASIC_URL = "https://image.tmdb.org/t/p/w500/"


## 영화 관련 SR ##
# 영화의 모든 데이터를 가져오는 Movie SR
class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


# 영화 리스트를 가져오는 Movie SR
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'tmdb_id', 'title', 'poster_path')


# 영화별 상세 페이지 가져오는 Movie SR
class MovieDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


## 댓글 관련 SR ##
# 댓글의 모든 데이터를 가져오는 Movie SR
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)


class CommentListSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user', )


