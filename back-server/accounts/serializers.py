from rest_framework import serializers
from .models import *
from movies.models import *
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            fields = '__all__'

    class MovieFollowSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = '__all__'
        
    like_articles = CommentSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'comment_like', 'movie', 'genre_likes', 'followings', 'followers', 'profile_img')
        read_only_fields = ('followings', 'followers')

class CustomSignupSerializer(RegisterSerializer):
    profile_img = serializers.CharField(min_length=0)
    genre_likes = serializers.JSONField(default=dict)