# DRF용 임포트
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 이용자 권한 확인용 임포트
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated


# 데이터 요구 방식 체크용 임포트
from rest_framework.decorators import permission_classes

# 데이터 반환용 임포트
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

# 내가 만들어 놓은 모델과 시리얼라이즈 가져오기
from .serializers import *
from .models import *

# 내가 설정한 유저 모델 가져오기 (user_like 이하 댓글과 영화 구현하기 위함임)
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer
User = get_user_model()

# 기타 함수 제작용 라이브러리
import random
import selenium


## 영화 관련 Views ##

# 영화 리스트 반환용 함수 (Post는 제작 과정에서 필요할 것 같아서 넣었슴다.)
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        Movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(Movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 제작 과정 끝나고 남길 GET 방식만 있는 함수
# @api_view(['GET'])
# def movie_list(request):
#     Movies = get_list_or_404(Movie)
#     serializer = MovieListSerializer(Movies, many=True)
#     return Response(serializer.data)


# 영화 상세 페이지 함수. 마찬가지로 제작과정에서 쓰시라고 Delete 넣었슴다. 끝나고 기능 삭제하겠슴다.
@api_view(['GET', 'DELETE'])
def movie_detail(request, movie_pk):
    # 여기서 검색은 PK값, 즉 tmdb_id를 기반으로 합니당~
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def movie_like(request, movie_pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=movie_pk)

    if user.like_comment.filter(pk=movie_pk).exists():
        user.like_comment.remove(comment)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        user.like_comment.add(comment)
        serializer = UserSerializer(user)
        return Response(serializer.data)


## 댓글 관련 Views ##

# 댓글 상세페이지. (조회, 삭제, 수정)
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 댓글 제작용 함수
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(status=status.HTTP_201_CREATED)

# 댓글 리스트 조회용 함수
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


# 댓글 좋아요 만들기/지우기 함수
@api_view(['POST'])
def comment_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user

    if user.user_like_comment.filter(pk=comment_pk).exists():
        user.user_like_comment.remove(comment)
        serializer = CommentSerializer(user)
        return Response(serializer.data)
    else:
        user.user_like_comment.add(comment)
        serializer = CommentSerializer(user)
        return Response(serializer.data)
    
"""
# 영화와 댓글에서의 유저 상호 작용 Many to Many 필드
class Movie(models.Model):
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_like_movies", symmetrical=True)

class Comment(models.Model):
    comment_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_like_comment", symmetrical=True)
"""




"""
여기서 부터는 보류한 기능들 입니다.

1. 주간 BOX office 순위 보기
from datetime import datetime, timedelta

# 오늘 날짜를, 박스오피스 API 검색에 맞는 형식으로 만들어주기
target_date = datetime.today().strftime("%Y%m%d")
BOX_URL = "https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=ce10aa520981b26cce4565d991bf011b&targetDt="

@api_view(['GET'])
def boxoffice(request):
    request = (f"{BOX_URL}+{target_date}")
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)         
    return Response(json_object)

2. 글 조회수 구현 기능



"""





