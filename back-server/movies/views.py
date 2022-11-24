# DRF용 임포트
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
import requests
import json


## 영화 관련 Views ##



# 영화 리스트 반환용 함수 (Post는 제작 과정에서 필요할 것 같아서 넣었슴다.)
@api_view(['GET', 'POST'])
def movie_list(request):
    print(request.user)
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



# vote_average를 기준으로 상위 20개 반환
@api_view(['GET'])
def top_rated(request):
    movies = Movie.objects.order_by('-vote_average')[0:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# popularity를 기준으로 상위 20개 반환
@api_view(['GET'])
def popular(request):
    movies = Movie.objects.order_by('-popularity')[0:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)







# 영화 상세 페이지 함수. 마찬가지로 제작과정에서 쓰시라고 Delete 넣었슴다. 끝나고 기능 삭제하겠슴다.
@api_view(['GET', 'DELETE'])
def movie_detail(request, movie_pk):
    # 여기서 검색은 PK값, 즉 tmdb_id를 기반으로 합니당~
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if movie.movie_like_users.filter(pk=request.user.pk).exists():
        movie.movie_like_users.remove(request.user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.movie_like_users.add(request.user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

# @api_view(['GET'])
# def movies_search(request):
#     movies = Movie.objects.all()
#     serializer = MovieSearchSerializer(movies, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)




## 댓글 관련 Views ##

# 댓글 상세페이지. (조회, 삭제, 수정)
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 댓글 제작용 함수
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        return Response(status=status.HTTP_201_CREATED)


# 댓글 리스트 조회용 함수
@api_view(['GET'])
def comment_list(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        comments = movie.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



# 댓글 좋아요 만들기/지우기 함수
@api_view(['POST'])
def comment_like(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.comment_like_users.filter(pk=request.user.pk).exists():
        comment.comment_like_users.remove(request.user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        comment.comment_like_users.add(request.user)
        serializer = CommentSerializer(comment)
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

### 이 아래는 API 기반 조회 및 검색 + 자동 DB화 로직입니당~


str_to_int = {
    '액션' : 28,
    '애니메이션' : 16,
    '드라마' : 18,
    '범죄' : 80,
    '멜로/로맨스' : 10749,
    '코미디' : 35,
    '스릴러' : 53,
    '공포(호러)' : 27,
    '미스터리' : 9648,
    'SF' : 878,
    '어드벤처' : 12,
    '판타지' : 14,
    '사극' : 36,
    '전쟁' : 10752,
    '가족' : 10751,
    '다큐멘터리' : 99,
    '뮤지컬' : 10402,
    '서부극(웨스턴)' : 37,
}

int_to_str = {
    28 : '액션',
    16 :'애니메이션',
    18 : '드라마',
    80 : '범죄',
    10749 : '멜로/로맨스',
    35 : '코미디',
    53 : '스릴러',
    27 : '공포(호러)',
    9648 : '미스터리',
    878 : 'SF',
    12 : '어드벤처',
    14 : '판타지',
    36 : '사극',
    10752 : '전쟁',
    10751 : '가족',
    99 : '다큐멘터리',
    10402 : '뮤지컬',
    37 : '서부극(웨스턴)',
}


TMDB_API_KEY = "f555794485796214438961ced766522e"

BASIC_URL = "https://image.tmdb.org/t/p/w500/"



@api_view(['GET'])
def get_new_movie(request):
    total_data = []

    for i in range(1, 2):
        request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                detail_url = f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key=f555794485796214438961ced766522e&language=ko-KR"
                detail = requests.get(detail_url).json()
                
                genre = []
                for genres in detail['genres']:
                    genre.append(genres["name"])

                if not movie['poster_path']:
                    movie['poster_path'] = "/d9C2H1qoFt9AL4DwRlqEEZK4hVa.jpg"

                if not detail['overview']:
                    detail['overview'] = ""
                
                if not detail['runtime']:
                    detail['runtime'] = 120
                
                if not movie['popularity']:
                    movie['popularity'] = 100

                if not movie['original_title']:
                    movie['original_title'] = "no_title"


                data = {
                    'pk': movie['id'],
                    'tmdb_id': movie['id'],
                    'title': movie['title'],
                    'original_title': movie['original_title'],
                    'release_date': movie['release_date'],
                    'runtime': detail['runtime'],
                    'overview': detail['overview'],
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'poster_path': BASIC_URL+movie['poster_path'],
                    'adult': movie['adult'],
                    'genre': genre,
                }

            
                total_data.append(data)



                if Movie.objects.filter(tmdb_id=movie['id']):
                    pass
                else:
                    serializer = MovieInputSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()

    return Response(total_data)



@api_view(['GET'])
def movie_search(request, word):
    total_data = []
    request_url = f"https://api.themoviedb.org/3/search/movie?api_key=f555794485796214438961ced766522e&language=ko-KR&query={word}&page=1&include_adult=true"
    movies = requests.get(request_url).json()

    for movie in movies['results']:
        if movie.get('release_date', ''):
            detail_url = f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key=f555794485796214438961ced766522e&language=ko-KR"
            detail = requests.get(detail_url).json()
            
            genre = []
            for genres in detail['genres']:
                genre.append(genres["name"])

            if not movie['poster_path']:
                movie['poster_path'] = "/d9C2H1qoFt9AL4DwRlqEEZK4hVa.jpg"

            if not detail['overview']:
                detail['overview'] = ""
            
            if not detail['runtime']:
                detail['runtime'] = 120
            
            if not movie['popularity']:
                movie['popularity'] = 100

            if not movie['original_title']:
                movie['original_title'] = "no_title"
                
            if not movie['vote_average']:
                movie['vote_average'] = 0


            data = {
                'pk': movie['id'],
                'tmdb_id': movie['id'],
                'title': movie['title'],
                'original_title': movie['original_title'],
                'release_date': movie['release_date'],
                'runtime': detail['runtime'],
                'overview': detail['overview'],
                'popularity': movie['popularity'],
                'vote_average': movie['vote_average'],
                'vote_count': movie['vote_count'],
                'poster_path': BASIC_URL+movie['poster_path'],
                'adult': movie['adult'],
                'genre': genre,
            }

            total_data.append(data)

            if Movie.objects.filter(tmdb_id=movie['id']):
                pass
            else:
                serializer = MovieInputSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    
    return Response(total_data)



@api_view(['GET'])
def get_genre_movie(request, genre_name):
    genre_code = str_to_int[genre_name]
    total_data = []


    for i in range(1, 2):
        request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                detail_url = f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key=f555794485796214438961ced766522e&language=ko-KR"
                detail = requests.get(detail_url).json()
                
                genre = []
                for genres in detail['genres']:
                    genre.append(genres["name"])

                data = {
                    "pk": movie['id'],
                    'tmdb_id': movie['id'],
                    'title': movie['title'],
                    'original_title': movie['original_title'],
                    'release_date': movie['release_date'],
                    'vote_average': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'overview': detail['overview'],
                    'popularity': movie['popularity'],
                    'poster_path': BASIC_URL+movie['poster_path'],
                    'adult': movie['adult'],
                    'genre': genre,
                    'runtime': detail['runtime'],
                }

                total_data.append(data)
                

    return Response(total_data)

