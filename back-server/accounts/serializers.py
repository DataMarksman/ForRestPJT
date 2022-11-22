from rest_framework import serializers
from .models import *
from movies.models import *
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()


# 유저 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = '__all__'
        

# 프로필 시리얼라이저
class ProfileSerializer(serializers.ModelSerializer):
    
    class CommentSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Comment
            fields = '__all__'


    class MovieLikeSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = '__all__'
        
    like_articles = CommentSerializer(many=True, read_only=True)
    articles = CommentSerializer(many=True, read_only=True)
    keep_movies = MovieLikeSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('pk', 'user', 'like_articles', 'comment', 'keep_movies', 'genre_likes', 'followings', 'followers', 'profile_img')
        read_only_fields = ('followings', 'followers')


# 기존에 있는 유저 필드에 더해서, 프로필 사진과 선호 장르 추가하여 진행하기 위한 시리얼라이저
class CustomSignupSerializer(RegisterSerializer):
    profile_img = serializers.CharField(min_length=0)
    genre_likes = serializers.JSONField(default=dict)
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_img'] = self.validated_data.get('profile_img', '')
        data['genre_likes'] = self.validated_data.get('genre_likes', '')
        return data