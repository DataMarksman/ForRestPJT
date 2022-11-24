from rest_framework import serializers
from .models import *
from movies.models import *
from movies.serializers import *
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()


# 유저 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'



# 프로필 시리얼라이저
class ProfileSerializer(serializers.ModelSerializer):
    
<<<<<<< HEAD:final-pjt-back/accounts/serializers.py
    class CommentSerializer(serializers.ModelSerializer):
=======
    class UserCommentSerializer(serializers.ModelSerializer):
        
        class UserMovieSerializer(serializers.ModelSerializer):
            
            class Meta:
                model = Movie
                fields = ('tmdb_id', 'title', 'poster_path')

        movie = UserMovieSerializer(read_only=True)
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b:back-server/accounts/serializers.py
        
        class Meta:
            model = Comment
            fields = '__all__'


    class MovieLikeSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
<<<<<<< HEAD:final-pjt-back/accounts/serializers.py
            fields = '__all__'
        
    like_articles = CommentSerializer(many=True, read_only=True)
    articles = CommentSerializer(many=True, read_only=True)
    keep_movies = MovieLikeSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_articles', 'comment', 'keep_movies', 'genre_likes', 'followings', 'followers', 'profile_img')
        read_only_fields = ('followings', 'followers')
=======
            fields = ('tmdb_id', 'title', 'poster_path',)

    class ProfileUserSerializer(serializers.ModelSerializer):
        
        class DeepUserSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('id', 'username',)
        
        followers = DeepUserSerializer(many=True, read_only=True)
        followings = DeepUserSerializer(many=True, read_only=True)
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'followers', 'followings', 'nick_name')

    user_like_movies = MovieLikesSerializer(many=True, read_only=True)
    comment_set = UserCommentSerializer(many=True, read_only=True)
    followers = ProfileUserSerializer(many=True, read_only=True)
    followings = ProfileUserSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'nick_name', 'user_like_movies', 'comment_set', 'followers', 'followings')



>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b:back-server/accounts/serializers.py


# 기존에 있는 유저 필드에 더해서, 프로필 사진과 선호 장르 추가하여 진행하기 위한 시리얼라이저
class CustomSignupSerializer(RegisterSerializer):
    profile_img = serializers.CharField(min_length=0)
    genre_likes = serializers.JSONField(default=dict)
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_img'] = self.validated_data.get('profile_img', '')
        data['genre_likes'] = self.validated_data.get('genre_likes', '')
        return data

