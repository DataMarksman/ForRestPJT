
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *

from movies.serializers import *
from movies.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

"""
# 영화와 댓글에서의 유저 상호 작용 Many to Many 필드
class Movie(models.Model):
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_like_movies", symmetrical=True)

class Comment(models.Model):
    comment_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_like_comment", symmetrical=True)
"""

# 프로필 조회하면 한방에 관련 정보 다 주기 위함임.
# 만약 수정을 원하면 PUT으로 수정하도록 함
# @api_view(['GET', 'PUT'])
# def profile_or_edit(request, user_id):
#     user = User.objects.get(pk=user_id)
#     if request.method == 'GET':
#         serializer = ProfileSerializer(user)
#         return Response(serializer.data)
    
#     elif request.user.is_authenticated:
#         serializer = ProfileSerializer(data=request.data, instance=user)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

@api_view(['GET', 'PUT'])
def profile_or_edit(request, user_id):
    user = User.objects.get(pk=user_id)
    
    my_movies = Movie.movie_like_users.filter(user_id=user_id)
    my_comments = Comment.objects.filter(user_id=user_id)

    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    elif request.user.is_authenticated:

        serializer = ProfileSerializer(data=request.data, instance=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



# 유저가 같은 테이블의 유저를 참조하여, 팔로잉 팔로우 합니다.
@api_view(['POST'])
def follow(request, user_id):
    partner = User.objects.get(pk=user_id)
    if partner != request.user:           
        if partner.followers.filter(pk=request.user.pk).exists():
            partner.followers.remove(request.user)   
            
        else:
            partner.followers.add(request.user)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)



