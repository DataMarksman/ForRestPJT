from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm
from .serializers import *

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

# # 프로필 조회하면 한방에 관련 정보 다 주기 위함임.
# # 만약 수정을 원하면 PUT으로 수정하도록 함
# @api_view(['GET', 'PUT'])
# def profile(request, user_id):

#     user = get_object_or_404(get_user_model(), id=user_id)
#     if request.method == 'GET':
#         serializer = ProfileSerializer(user)
#         return Response(serializer.data)
    
#     elif request.user.is_authenticated:
#         serializer = ProfileSerializer(data=request.data, instance=user)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)


# # 유저가 같은 테이블의 유저를 참조하여, 팔로잉 팔로우 합니다.
# @api_view(['POST'])
# def follow(request, user_id):
#     partner = get_object_or_404(User, id=user_id)
#     follower = request.user                     

#     if follower.followings.filter(id=user_id).exists():
#         follower.followings.remove(partner)   
        
#     else:
#         follower.followings.add(partner)
#     serializer = UserSerializer(follower)
#     return Response(serializer.data)




@api_view(['GET'])
def profile(request, username):
    user = User.objects.filter(username=username)    
    serializer = UserListSerializer(user,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request):
    you = get_object_or_404(get_user_model(), username = request.data.get('profileName'))
    me = request.user
    if you != me :
        # print(you.followers.filter(pk=me.pk))  
        if you.followers.filter(pk=request.user.pk).exists(): 
            you.followers.remove(me)
            following = False
        else : 
            you.followers.add(me)
            following = True
        context = {
            'following' : following,
            'follower_count' : you.followers.count(),
            'following_count' : you.followings.count()
        }
        return Response(context,status=status.HTTP_201_CREATED)

